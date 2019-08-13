from datetime import datetime

from flask import g
from models.transaction import Transaction
from ariadne import QueryType, MutationType, convert_kwargs_to_snake_case

query = QueryType()
mutation = MutationType()

"""
QUERIES
"""


@query.field("transaction")
def resolve_transaction(_, info, pk):
    return Transaction.query.get(int(pk))


@query.field("transactions")
@convert_kwargs_to_snake_case
def resolve_transactions(_, info, from_date=None, to_date=None, account=None, amount=None):
    tranx_q = Transaction.query

    if from_date is not None:
        tranx_q = tranx_q.filter(Transaction.date >= from_date)

    if to_date is not None:
        tranx_q = tranx_q.filter(Transaction.date <= to_date)

    if account is not None:
        tranx_q = tranx_q.filter(Transaction.line_items.contains([{'account': account}]))

    if amount is not None:
        tranx_q = tranx_q.filter(Transaction.line_items.contains([{'amount': amount}]))

    return list(map(lambda q: {
        "description": q.description,
        "date": q.date,
        "sum": q.sum,
        "id": q.id,
        "lineItems": q.line_items,
    }, tranx_q))


"""
MUTATIONS
"""


@mutation.field("addTransaction")
def resolve_add_transaction(_, info, amount, date, description):
    parsed_date = datetime.fromtimestamp(int(date) / 1000)

    transaction = Transaction(
        date=parsed_date,
        description=description
    )

    transaction.add_line_item(1, 1001, int(amount))
    transaction.add_line_item(2, 2001, int(amount))
    transaction.reconcile()

    g.db.add(transaction)
    g.db.commit()

    return {
        "description": transaction.description,
        "date": transaction.date,
        "lineItems": transaction.line_items,
        "id": transaction.id,
        "sum": transaction.sum,
    }
