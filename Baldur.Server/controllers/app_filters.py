from flask import Blueprint, request, g
from settings.database import Session
from helpers.authenticator import verify_token

from models.user import User


bp = Blueprint("filters", __name__)


@bp.before_app_request
def authenticate_token():
    """
    Open a db session (and save the session for the duration of the request),
    verify the JWT token, and grab the request's user (if any), save it
    as part of the request for future use.
    """
    g.db = Session()

    user = None
    auth_token = request.headers.get("Authorization")
    session_id = verify_token(auth_token)

    if session_id is not None:
        user = User.query.filter(User.session.has(id=session_id)).first()

    g.user = user


@bp.after_app_request
def after_request(response):
    if g.session is not None:
        g.session.close()

    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    header['Access-Control-Allow-Headers'] = 'origin content-type'

    return response

