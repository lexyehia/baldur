from flask import g
from graphene import Mutation, String, Boolean, Int
from .queries import User as UserType
from models.user import User as UserModel
from helpers.misc import map_instance


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
        user_type = map_instance(UserType, user)
        return user_type


class DeleteUser(Mutation):
    class Arguments:
        pk = Int()

    Output = Boolean

    @staticmethod
    def mutate(root, info, pk):
        user = g.db.query(UserModel).get(pk)
        g.db.delete(user)
        g.db.commit()
        return True


