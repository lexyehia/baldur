import jwt
import random
from pathlib import Path
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta
from models.session import Session
from flask import g

SECRET = "34trg345354hy463y43hge"


def hash_password(password):
    ph = PasswordHasher()
    pepper = random.choice(get_peppers_list())
    return ph.hash(password + pepper)


def verify_password(hashed_password, password):
    ph = PasswordHasher()
    peppers = get_peppers_list()

    for pepper in peppers:
        try:
            ph.verify(hashed_password, password + pepper)
            return True
        except VerifyMismatchError as e:
            print(e)

    return False


def get_peppers_list():
    path = Path(__file__) / "../../peppers.txt"
    file = open(path, "r")
    peppers = []
    for line in file:
        peppers.append(line)
    file.close()
    return peppers


def start_session(user):
    if user is None:
        return None

    user.session = Session()
    g.db.commit()
    return user.session.id


def create_token(session_id):
    payload = {
        "ssn": session_id,
        "exp": datetime.utcnow() + timedelta(minutes=20),
        "nbf": datetime.utcnow(),
        "iss": "Baldur"
    }

    token_bytes = jwt.encode(payload, SECRET, algorithm="HS256")
    return str(token_bytes, "utf-8")


def verify_token(token):
    """
    Takes a token string and verifies its authenticity, then returns
    the embedded session guid string
    """
    if type(token) is not str:
        return None

    if "Bearer " in token:
        token = token.replace("Bearer ", "")

    try:
        decoded_token = jwt.decode(token,
                                   SECRET,
                                   issuer="Baldur",
                                   algorithms="HS256")
        return decoded_token["ssn"]

    except Exception as e:
        print(e)
        return None
