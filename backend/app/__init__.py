from flask import Flask
import flask_login

from . import api
from . import auth


app = Flask(__name__)
app.secret_key = 'super secret string'

# Registrations
app.register_blueprint(api.bp)


if __name__ == "__main__":
    app.run()
