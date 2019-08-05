from data.user import model
from graphene_sqlalchemy import SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = model.User

