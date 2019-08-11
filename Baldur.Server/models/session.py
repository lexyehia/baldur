from settings.database import Base
from sqlalchemy import Column, Integer, ForeignKey, event
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4


class Session(Base):
    __tablename__ = "sessions"

    # Columns
    id = Column(UUID(as_uuid=True), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    # Relationships
    user = relationship("User", back_populates="session")


@event.listens_for(Session, 'before_insert')
def assign_uuid(mapper, connection, target):
    target.id = target.id or uuid4()
