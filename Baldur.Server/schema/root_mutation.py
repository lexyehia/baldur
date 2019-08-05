from graphene import ObjectType
from .user.mutations import *


class RootMutation(ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
