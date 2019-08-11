from graphene import ObjectType

from schema.transaction.mutations import TransactionMutation
from .user.mutations import UserMutation


class RootMutation(UserMutation, TransactionMutation, ObjectType):
    pass
