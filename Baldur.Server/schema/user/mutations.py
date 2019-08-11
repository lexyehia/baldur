from typing import Optional

from flask import g, abort
from graphene import *

from helpers.decorators import restricted
from .queries import User
from models.user import User as UserModel
from helpers.authenticator import hash_password, create_token


class CreateUser(Mutation):
    class Arguments:
        email = String()
        first_name = String()
        last_name = String()
        password = String()

    Output = User

    @staticmethod
    def mutate(root, info, last_name: str, email: str, first_name: str, password: str) -> UserModel:
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
    def mutate(root, info, pk: int) -> bool:
        user = User.get_query(info).get(pk)
        g.db.delete(user)
        g.db.commit()
        return True


class NewSession(Mutation):
    class Arguments:
        email = String()
        password = String()

    Output = String

    @staticmethod
    def mutate(root, info, email: str, password: str) -> Optional[str]:
        user = User.get_query(info).filter_by(email=email).first()

        if not isinstance(user, UserModel) or not user.verify_password(password):
            return abort(400)

        session_id = user.start_session()

        if not session_id:
            return abort(500)

        return create_token(session_id)


class EndSession(Mutation):
    class Arguments:
        pass

    Output = Boolean

    @staticmethod
    @restricted
    def mutate(root, info) -> bool:
        g.user.end_session()
        return True


class UserMutation(ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    login = NewSession.Field()
    logout = EndSession.Field()
