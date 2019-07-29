import jwt
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta

SECRET = "34trg345354hy463y43hge"

def hash_password(password):
    ph = PasswordHasher()
    return ph.hash(password)


def verify_password(hash, password):
    ph = PasswordHasher()
    try:
        return ph.verify(hash, password)
    except VerifyMismatchError as e:
        print(e)
        return False


def create_token(user_id):
    payload = {
        "user": user_id,
        "exp" : datetime.utcnow() + timedelta(minutes=10),
        "nbf" : datetime.utcnow(),
        "iss" : "Baldur"
    }

    return jwt.encode(payload, SECRET, algorithm="HS256")


def verify_token(token):
    try:
        decoded_token = jwt.decode(token, SECRET, issuer="Baldur", algorithms="HS256")
        return decoded_token["user"]
    except Exception as e:
        print(e)
        return None
