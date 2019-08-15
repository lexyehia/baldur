from settings.database import Base
from sqlalchemy import Column, Integer, String


class Account(Base):
    __tablename__ = 'accounts'

    id: int = Column(Integer, primary_key=True)
    number: int = Column(Integer, nullable=False)
    name: str = Column(String, nullable=False)
    type: int = Column(Integer, nullable=False)
