from settings.database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.types import TypeDecorator


class LineItem(object):

    def __init__(self, type, amount, account):
        self.type = type
        self.amount = amount
        self.account = account

    def as_dict(self):
        return {'type': self.type, 'amount': self.amount, 'account': self.account}


class LineItemType(TypeDecorator):
    impl = JSONB

    def process_bind_param(self, value, dialect):
        return value.as_dict()

    def process_result_value(self, value, dialect):
        return LineItem(**value)


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    description = Column(String, default='')
    date = Column(Date, nullable=False)
    line_items = Column(ARRAY(LineItemType), server_default='{}')
    sum = Column(Integer, nullable=False)


