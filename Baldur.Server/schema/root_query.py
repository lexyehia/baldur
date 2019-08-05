from graphene import *
from .user.queries import UserQuery


class RootQuery(UserQuery, ObjectType):
    pass
