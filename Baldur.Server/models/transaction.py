from settings.database import Base
from sqlalchemy import Column, Integer, String, Date, event
from sqlalchemy.dialects.postgresql import JSONB


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    description = Column(String, default='')
    date = Column(Date, nullable=False)
    line_items = Column(JSONB)
    sum = Column(Integer, nullable=False)

    def add_line_item(self, line_type, account, amount):
        if type(line_type) is not int:
            raise TypeError("line_type is not an int")

        if type(account) is not int:
            raise TypeError("account is not an int")

        if type(amount) is not int:
            raise TypeError("amount is not an int")

        line_item = {
            'type': line_type,
            'account': account,
            'amount': amount,
        }

        if type(self.line_items) is not list:
            self.line_items = []

        self.line_items.append(line_item)
        return self

    def reconcile(self):
        self.sum = 0

        if type(self.line_items) is list:
            for line_item in self.line_items:
                if line_item['type'] == 1:
                    self.sum += line_item['amount']
                elif line_item['type'] == 2:
                    self.sum -= line_item['amount']

        if self.sum != 0:
            raise Exception("Transaction sum not reconciled to 0")
