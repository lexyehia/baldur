from flask import Blueprint
from settings.database import Session
from models.user import User

ctrl = Blueprint("api", __name__, url_prefix="/api")

@ctrl.route("/bob/<page>")
def show(page):
    session = Session()
    user = User(first_name="Bob", last_name="Rae", email="bob@rae.com")
    session.add(user)
    session.commit()
    return f"User ID# {user.id}"


