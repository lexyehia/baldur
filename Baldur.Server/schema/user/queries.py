from flask import g
from models.user import User as UserModel
from graphene import *
from graphene_sqlalchemy import SQLAlchemyObjectType
from helpers.decorators import restricted


class User(SQLAlchemyObjectType):
    """
    UserType returned as a DTO back through GraphQL
    """
    class Meta:
        model = UserModel
        exclude_fields = ("hashed_password",)


class UserQuery(ObjectType):
    """
    GraphQL queries re users, this class is inherited by the RootQuery class
    """
    users = List(User)
    user = Field(User, pk=ID(required=True))
    me = Field(User)

    @staticmethod
    def resolve_users(parent, info):
        query = g.db.query(UserModel)
        return query.all()

    @staticmethod
    def resolve_user(parent, info, pk):
        query = g.db.query(UserModel)
        return query.get(int(pk))

    @staticmethod
    @restricted
    def resolve_me(parent, info):
        return g.user


