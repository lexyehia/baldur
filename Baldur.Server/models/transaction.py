from settings.database import Base
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.dialects.postgresql import JSONB, ARRAY
from sqlalchemy.types import TypeDecorator


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    description = Column(String, default='')
    date = Column(Date, nullable=False)
    line_items = Column(JSONB)
    sum = Column(Integer, nullable=False)


