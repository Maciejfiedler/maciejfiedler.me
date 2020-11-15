from flask import Blueprint
from flask_graphql import GraphQLView
import graphene

bp = Blueprint('api', __name__, url_prefix='/api')


class Query(graphene.ObjectType):
    redis_status = graphene.String()
    redis_description = graphene.String()
    redis_intrests = graphene.String()

    def resolve_redis_status(self, info):
        return "Good"

    def resolve_redis_description(self, info):
        return """My name is Maciej Fiedler. I am 15 years old and i like to
        programm. Besides programming I also do Ju-Jitsu, play Tennis and
        Videogames."""

    def resolve_redis_intrests(self, info):
        return """Backend Systems, Overwatch, Tennis, Physics, Ju-Jitsu, Design,
              Linux, Music, PCs, Minecraft, Learning Programming languages and
              technologies, New technologies(RISC-V, Quantum Computing etc.)"""


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
    redisStatus,
    redisDescription,
    redisIntrests
  }
''')}"""
