from models import *
from settings.database import Base
from flask import g


def get_hydrated_base():
    return Base
