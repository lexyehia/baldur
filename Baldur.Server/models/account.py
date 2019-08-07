from settings.database import Base
from sqlalchemy import Column, Integer, String


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    number = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    type = Column(Integer, nullable=False)
