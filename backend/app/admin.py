from flask_admin._compat import VER
from flask_admin.babel import gettext
from flask_admin.base import BaseView, expose
from jinja2 import Markup
from flask import request
import warnings
import shlex
import logging
from flask import redirect, url_for, render_template
import flask_admin
import flask_login
from flask_admin import expose, BaseView

from . import db
from . import auth


class MyAdminIndexView(flask_admin.AdminIndexView):
    def is_accessible(self):
        return flask_login.current_user.is_authenticated


# Set up logger
log = logging.getLogger("flask-admin.redis")


class CommandError(Exception):
    pass


class TextWrapper(str):
    pass


class RedisCli(BaseView):
    def is_accessible(self):
        return flask_login.current_user.is_authenticated

    shlex_check = True

    remapped_commands = {
        'del': 'delete'
    }

    excluded_commands = set(('pubsub', 'set_response_callback', 'from_url'))

    def __init__(self, redis,
                 name=None, category=None, endpoint=None, url=None):
        super(RedisCli, self).__init__(name, category, endpoint, url)

        self.redis = redis

        self.commands = {}

        self._inspect_commands()
        self._contribute_commands()

        if self.shlex_check and VER < (2, 7, 3):
            warnings.warn('Warning: rediscli uses shlex library and it does '
                          'not work with unicode until Python 2.7.3. To '
                          'remove this warning, upgrade to Python 2.7.3 or '
                          'suppress it by setting shlex_check attribute '
                          'to False.')

    def _inspect_commands(self):
        for name in dir(self.redis):
            if not name.startswith('_'):
                attr = getattr(self.redis, name)
                if callable(attr) and name not in self.excluded_commands:
                    doc = (getattr(attr, '__doc__', '') or '').strip()
                    self.commands[name] = (attr, doc)

        for new, old in self.remapped_commands.items():
            self.commands[new] = self.commands[old]

    def _contribute_commands(self):
        self.commands['help'] = (self._cmd_help, 'Help!')

    def _execute_command(self, name, args):
        # Do some remapping
        new_cmd = self.remapped_commands.get(name)
        if new_cmd:
            name = new_cmd

        # Execute command
        if name not in self.commands:
            return self._error(gettext('Cli: Invalid command.'))

        handler, _ = self.commands[name]
        return self._result(handler(*args))

    def _parse_cmd(self, cmd):
        if VER < (2, 7, 3):
            # shlex can't work with unicode until 2.7.3
            return tuple(x.decode('utf-8') for x in shlex.split(cmd.encode('utf-8')))

        return tuple(shlex.split(cmd))

    def _error(self, msg):
        return Markup('<div class="error">%s</div>' % msg)

    def _result(self, result):
        return self.render('admin/rediscli/response.html',
                           type_name=lambda d: type(d).__name__,
                           result=result)

    # Commands
    def _cmd_help(self, *args):
        if not args:
            help = 'Usage: help <command>.\nList of supported commands: '
            help += ', '.join(n for n in sorted(self.commands))
            return TextWrapper(help)

        cmd = args[0]
        if cmd not in self.commands:
            raise CommandError('Invalid command.')

        help = self.commands[cmd][1]
        if not help:
            return TextWrapper('Command does not have any help.')

        return TextWrapper(help)

    # Views
    @expose('/')
    def console_view(self):
        return self.render('admin/rediscli/console.html')

    @expose('/run/', methods=('POST',))
    def execute_view(self):
        try:
            cmd = request.form.get('cmd').lower()
            if not cmd:
                return self._error('Cli: Empty command.')

            parts = self._parse_cmd(cmd)
            if not parts:
                return self._error('Cli: Failed to parse command.')

            return self._execute_command(parts[0], parts[1:])
        except CommandError as err:
            return self._error('Cli: %s' % err)
        except Exception as ex:
            log.exception(ex)
            return self._error('Cli: %s' % ex)
