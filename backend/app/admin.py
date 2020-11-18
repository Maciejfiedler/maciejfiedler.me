from flask import redirect, url_for, render_template
import flask_admin
import flask_login
from flask_admin import expose
from flask_admin.contrib import rediscli

from . import db
from . import auth


class MyAdminIndexView(flask_admin.AdminIndexView):

    @expose('/')
    def index(self):
        if auth.is_logged_in():
            return render_template('admin.html')
        else:
            return "You're not logged in buddy :c"
