from graphene import ObjectType
from .user.mutations import UserMutation


class RootMutation(UserMutation, ObjectType):
    pass
