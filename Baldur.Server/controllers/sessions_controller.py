from flask import Blueprint, request, abort, g
from models.user import User
import helpers.authenticator as auth

ctrl = Blueprint("sessions", __name__, url_prefix="/sessions")


@ctrl.route("", methods=["PUT"])
def start_session():
    json = request.get_json()

    if json is None:
        return abort(403)

    user = g.db.query(User).filter_by(email=json["email"]).first()

    if user is None:
        return abort(403)

    if auth.verify_password(user.encoded_password, json["password"]):
        session_id = auth.start_session(user.id)
        return auth.create_token(session_id)

    return abort(403)


@ctrl.route("", methods=["DELETE"])
def end_session():
    if g.user and g.user.session:
        g.user.session = None
        g.db.commit()

    return "", 200

