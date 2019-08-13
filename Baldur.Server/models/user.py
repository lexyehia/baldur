from typing import Optional

from flask import g

from helpers.authenticator import verify_password
from models.session import Session
from settings.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"

    # Columns
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)

    # Relationships
    session = relationship("Session", back_populates="user", uselist=False, cascade="all, delete-orphan")

    def start_session(self) -> Optional[str]:
        self.end_session()
        self.session = Session()
        g.db.commit()
        return str(self.session.id)

    def end_session(self):
        if self.session:
            g.db.delete(self.session)
            g.db.commit()

    def verify_password(self, password: str) -> bool:
        return verify_password(self.hashed_password, password)
