from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgres://postgres:12345@localhost:5432/baldur", echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
