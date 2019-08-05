from flask import abort, g
from models.user import User


def restricted(f):
    """
    Decorate a route so that it returns a 401 if a 'user' is not authenticated
    on the request
    """
    def wrapper(*args, **kwargs):
        if isinstance(g.user, User):
            return f(*args, **kwargs)
        else:
            return abort(401)

    return wrapper

