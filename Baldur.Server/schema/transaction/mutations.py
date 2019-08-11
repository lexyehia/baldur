from flask import g
from graphene import *
from .queries import Transaction as TransactionType
from models.transaction import Transaction as TransactionModel
from datetime import datetime


class AddTransaction(Mutation):
    class Arguments:
        amount = Int()
        date = Float()
        description = String()

    Output = TransactionType

    @staticmethod
    def mutate(root, info, amount, date, description):
        parsed_date = datetime.fromtimestamp(date / 1000)

        transaction = TransactionModel(
            date=parsed_date,
            description=description
        )

        transaction.add_line_item(1, 1001, amount)
        transaction.add_line_item(2, 2001, amount)
        transaction.reconcile()

        g.db.add(transaction)
        g.db.commit()

        return TransactionType(
            id=transaction.id,
            line_items=transaction.line_items,
            description=transaction.description,
            sum=transaction.sum
        )


class TransactionMutation(ObjectType):
    add_transaction = AddTransaction.Field()
