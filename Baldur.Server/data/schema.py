from graphene import ObjectType, Schema, List, String, Field
from .session.model import Session
from .user.model import User as UserModel
from .user.queries import User
from .user.mutations import CreateUser
from helpers.decorators import restricted


class Query(ObjectType):
    users = List(User)
    user = Field(User, q=String())

    def resolve_users(parent, info):
        query = User.get_query(info)
        return query.all()

    @restricted
    def resolve_user(self, info, q):
        user_query = User.get_query(info)
        users = user_query.filter(UserModel.id == int(q))
        return users.first()


class Mutation(ObjectType):
    create_user = CreateUser.Field()


schema = Schema(query=Query, mutation=Mutation, types=[
    User,
])
