from models import transaction
from graphene import *
from graphene_sqlalchemy import SQLAlchemyObjectType


class Transaction(SQLAlchemyObjectType):
    """
    UserType returned as a DTO back through GraphQL
    """
    class Meta:
        model = transaction.Transaction


class TransactionQuery(ObjectType):
    """
    GraphQL queries re users, this class is inherited by the RootQuery class
    """
    transactions = List(Transaction)
    transaction = Field(Transaction, pk=Int())

    @staticmethod
    def resolve_transactions(parent, info):
        query = Transaction.get_query(info)
        return query.all()

    @staticmethod
    def resolve_transaction(self, info, pk):
        query = Transaction.get_query(info)
        return query.get(pk)
