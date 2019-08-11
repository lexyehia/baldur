from graphene import *

from .transaction.queries import TransactionQuery
from .user.queries import UserQuery


class RootQuery(UserQuery, TransactionQuery, ObjectType):
    pass
