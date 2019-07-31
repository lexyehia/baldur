from graphene import ObjectType, Schema, List, String, Field
from graphene_sqlalchemy import SQLAlchemyConnectionField
from schemas.user import User, UserModel
from helpers.authenticator import restricted

class Query(ObjectType):
    users = List(User)
    user = Field(User, q=String())

    def resolve_users(self, info):
        query = User.get_query(info)
        return query.all()

    def resolve_user(self, info, q=None):
        user_query = User.get_query(info)
        users = user_query.filter(UserModel.id == int(q))
        return users.first()


schema = Schema(query=Query, types=[
    User,
])
