from flask import g
from graphene import Mutation, String
from .queries import User as UserType
from .model import User as UserModel


class CreateUser(Mutation):
    class Arguments:
        email = String()
        first_name = String()
        last_name = String()

    Output = UserType

    @staticmethod
    def mutate(root, info, last_name, email, first_name):
        user = UserModel(email=email, first_name=first_name, last_name=last_name)
        g.db.add(user)
        g.db.commit()
        return UserType()
