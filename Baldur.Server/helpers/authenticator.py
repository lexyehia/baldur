import jwt
import random
from pathlib import Path
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta

SECRET = "34trg345354hy463y43hge"

def hash_password(password):
    ph = PasswordHasher()
    pepper = random.choice(get_peppers_list())
    return ph.hash(password + pepper)


def verify_password(hash, password):
    ph = PasswordHasher()
    peppers = get_peppers_list()
    for pepper in peppers:
        try:
            ph.verify(hash, password + pepper)
            return True
        except VerifyMismatchError as e:
            print(e)

    return False


def get_peppers_list():
    path = Path(__file__) / "../../references/peppers.txt"
    file = open(path, "r")
    peppers = []
    for line in file:
        peppers.append(line)
    file.close()
    return peppers


def create_token(user_id):
    payload = {
        "user": user_id,
        "exp" : datetime.utcnow() + timedelta(minutes=20),
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
