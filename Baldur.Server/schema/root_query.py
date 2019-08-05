from graphene import ObjectType, List, String, Field
from models.user import User as UserModel
from .user.queries import User
from helpers.decorators import restricted


class RootQuery(ObjectType):
    users = List(User)
    user = Field(User, q=String())

    @staticmethod
    def resolve_users(parent, info):
        query = User.get_query(info)
        return query.all()

    @restricted
    def resolve_user(self, info, q):
        user_query = User.get_query(info)
        users = user_query.filter(UserModel.id == int(q))
        return users.first()





