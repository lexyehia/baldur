from flask import g
import datetime
from models.transaction import Transaction as TransactionModel
from graphene import *
from graphene_sqlalchemy import SQLAlchemyObjectType


class LineItem(ObjectType):
    amount = Int()
    account = Int()
    type = Int()


class Transaction(SQLAlchemyObjectType):
    """
    Transaction returned as a DTO back through GraphQL
    """

    class Meta:
        model = TransactionModel

    line_items = List(LineItem)


class TransactionQuery(ObjectType):
    """
    GraphQL queries re transactions, this class is inherited by the RootQuery class
    """
    transactions = List(Transaction, from_date=Date(), to_date=Date(), account=Int(), amount=Int())
    transaction = Field(Transaction, pk=ID(required=True))

    @staticmethod
    def resolve_transactions(parent, info, from_date=None, to_date=None, account=None, amount=None):
        query = g.db.query(TransactionModel)

        if from_date is not None:
            query = query.filter(TransactionModel.date >= from_date)

        if to_date is not None:
            query = query.filter(TransactionModel.date <= to_date)

        if account is not None:
            query = query.filter(TransactionModel.line_items.contains([{'account': account}]))

        if amount is not None:
            query = query.filter(TransactionModel.line_items.contains([{'amount': amount}]))

        return query.all()

    @staticmethod
    def resolve_transaction(self, info, pk):
        query = g.db.query(TransactionModel)
        return query.get(int(pk))
