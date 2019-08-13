from ariadne import convert_kwargs_to_snake_case, QueryType, MutationType
from models.user import User
from helpers.authenticator import hash_password, create_token
from flask import g, abort

query = QueryType()
mutation = MutationType()
user_resolvers = [query, mutation]

"""
QUERIES
"""


@query.field("me")
def resolve_me(_, info):
    if isinstance(g.user, User):
        return {
            'id': g.user.id,
            'firstName': g.user.first_name,
            'lastName': g.user.last_name,
            'email': g.user.email,
        }

    return None


@query.field("users")
def resolve_users(_, info):
    users_result = g.db.query(User.email, User.first_name, User.last_name, User.id).all()

    users_dto = map(lambda u: {
        "id": u.id,
        "firstName": u.first_name,
        "lastName": u.last_name,
        "email": u.email,
    }, users_result)

    return list(users_dto)


@query.field("user")
@convert_kwargs_to_snake_case
def resolve_user(_, info, pk):
    user = User.query.get(int(pk))

    if not user:
        return None

    return {
        "id": user.id,
        "firstName": user.first_name,
        "lastName": user.last_name,
        "email": user.email,
    }


"""
MUTATIONS
"""


@mutation.field("createUser")
@convert_kwargs_to_snake_case
def resolve_create_user(_, info, email, password, first_name, last_name):
    user = User(
        email=email,
        first_name=first_name,
        last_name=last_name,
        hashed_password=hash_password(password),
    )

    g.db.add(user)
    g.db.commit()

    return user


@mutation.field("deleteUser")
def resolve_delete_user(_, info, pk):
    user = User.query.get(int(pk))
    g.db.delete(user)
    g.db.commit()
    return True


@mutation.field("login")
def resolve_login(_, info, email, password):
    user = User.query.filter_by(email=email).first()

    if not isinstance(user, User) or not user.verify_password(password):
        raise Exception("Invalid credentials")

    session_id = user.start_session()

    if not session_id:
        raise Exception("Could not start a new session")

    return create_token(session_id)


@mutation.field("logout")
def resolve_logout(_, info):
    g.user.end_session()
    return True
