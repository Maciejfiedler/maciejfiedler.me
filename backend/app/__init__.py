from flask import Flask, redirect, request, url_for
import flask_login
import flask_admin
from flask_admin.contrib import rediscli

from .admin import MyAdminIndexView
from . import api
from . import auth
from . import db


def create_app():
    app = Flask(__name__)
    app.secret_key = 'super secret string'

    # Assignings
    app.register_blueprint(api.bp)

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)

    admin = flask_admin.Admin(app, "Admin", index_view=MyAdminIndexView())

    # Functions
    @login_manager.user_loader
    def user_loader(email):
        return auth.user_loader(email)

    @login_manager.request_loader
    def request_loader(request):
        return auth.request_loader(request)

    @login_manager.unauthorized_handler
    def unauthorized_handler():
        return auth.unauthorized_handler()

    # Routes
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        return auth.login()

    @app.route('/logout')
    def logout():
        return auth.logout()

    return app
