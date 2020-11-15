from flask import Blueprint
from flask_admin import Admin, BaseView, expose

bp = Blueprint('admin', __name__, url_prefix='/admin')
admin = Admin(bp, name='posts',)


class Index(BaseView):
    expose('/')
    def index()
