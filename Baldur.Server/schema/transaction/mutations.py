from flask import g
import json
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
        trx = TransactionModel(
            date=datetime.fromtimestamp(date / 1000),
            description=description
        )

        trx.line_items = [
            {
                'account': 1,
                'type': 1,
                'amount': amount
            },
            {
                'account': 2,
                'type': 2,
                'amount': amount
            }
        ]

        trx.sum = 0

        g.db.add(trx)
        g.db.commit()

        rt = TransactionType(
            id=trx.id,
            line_items=trx.line_items,
            description=trx.description,
            sum=trx.sum
        )

        return rt


class TransactionMutation(ObjectType):
    add_transaction = AddTransaction.Field()
