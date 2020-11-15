from flask import Blueprint
from flask_graphql import GraphQLView
import graphene
from . import database as db

bp = Blueprint('api', __name__, url_prefix='/api')


class Query(graphene.ObjectType):
    my_status = graphene.String()
    my_description = graphene.String()
    my_intrests = graphene.String()

    def resolve_my_status(self, info):
        return f'{db.r.get("my_status")}'

    def resolve_my_description(self, info):
        return f'{db.r.get("my_description")}'

    def resolve_my_intrests(self, info):
        return f'{db.r.get("my_interests")}'


schema = graphene.Schema(query=Query)

bp.add_url_rule('/', view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    batch=True,
    graphiql=True
))


@bp.route("/result")
def result():
    return f"""{schema.execute('''
  query {
    myStatus,
    myDescription,
    myIntrests
  }
''')}"""
