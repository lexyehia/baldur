from sqlalchemy import create_engine
from flask import g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgres://postgres:12345@localhost:5432/baldur", echo=True)
Session = sessionmaker(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def get_db():
    if g is not None and g.db is not None:
        return g.db
