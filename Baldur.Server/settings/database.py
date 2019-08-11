from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine("postgres://postgres:12345@localhost:5432/baldur", echo=True)
Base = declarative_base()
session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=True))
Base.query = session.query_property()


def setup_db():
    from flask import g
    g.db = session


def close_db():
    from flask import g
    if g.db is not None:
        g.db.close()
