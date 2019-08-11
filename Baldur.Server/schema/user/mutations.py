from flask import g
from graphene import *
from .queries import User
from models.user import User as UserModel
from helpers.authenticator import hash_password


class CreateUser(Mutation):
    class Arguments:
        email = String()
        first_name = String()
        last_name = String()
        password = String()

    Output = User

    @staticmethod
    def mutate(root, info, last_name, email, first_name, password):
        user = UserModel(
            email=email,
            first_name=first_name,
            last_name=last_name,
            hashed_password=hash_password(password),
        )

        g.db.add(user)
        g.db.commit()

        return user


class DeleteUser(Mutation):
    class Arguments:
        pk = Int()

    Output = Boolean

    @staticmethod
    def mutate(root, info, pk):
        user = UserModel.query.get(pk)
        g.db.delete(user)
        g.db.commit()
        return True


class UserMutation(ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
