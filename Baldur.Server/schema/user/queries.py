from models import user
from graphene import *
from graphene_sqlalchemy import SQLAlchemyObjectType
from helpers.decorators import restricted


class User(SQLAlchemyObjectType):
    """
    UserType returned as a DTO back through GraphQL
    """
    class Meta:
        model = user.User
        exclude_fields = ("hashed_password",)


class UserQuery(ObjectType):
    """
    GraphQL queries re users, this class is inherited by the RootQuery class
    """
    users = List(User)
    user = Field(User, q=String())

    @staticmethod
    def resolve_users(parent, info):
        query = User.get_query(info)
        return query.all()

    @restricted
    def resolve_user(self, info, q):
        user_query = User.get_query(info)
        return user_query.get(int(q))
