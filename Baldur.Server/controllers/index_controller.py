from flask import Blueprint, g
from models.user import User

ctrl = Blueprint("api", __name__, url_prefix="/api")

@ctrl.route("/bob/<page>")
def show(page):
    user = User(first_name="Bob", last_name="Rae", email="bob@rae.com")
    g.db.add(user)
    g.db.commit()
    return f"User ID# {user.id}"


