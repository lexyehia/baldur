from models import user
from graphene_sqlalchemy import SQLAlchemyObjectType


class User(SQLAlchemyObjectType):
    class Meta:
        model = user.User
        exclude_fields = ("hashed_password",)
