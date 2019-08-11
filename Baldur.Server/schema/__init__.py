from models import *
from graphene import Schema, ObjectType

from schema.transaction.mutations import TransactionMutation
from schema.transaction.queries import TransactionQuery
from schema.user.mutations import UserMutation
from schema.user.queries import UserQuery


class RootQuery(
    UserQuery,
    TransactionQuery,
    ObjectType,
):
    pass


class RootMutation(
    UserMutation,
    TransactionMutation,
    ObjectType,
):
    pass


schema = Schema(query=RootQuery, mutation=RootMutation)
