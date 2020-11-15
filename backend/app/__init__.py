from flask import Flask


def create_app():
    app = Flask(__name__)

    # Admin
    from . import admin
    app.register_blueprint(admin.bp)

    # API
    #from . import api
    # app.register_blueprint(api.bp)

    return app
