from models import *
from settings.database import Base
from flask import g


def map_instance(target_cls, source_instance):
    if isinstance(source_instance, Base) and g.db is not None:
        g.db.refresh(source_instance)

    attrs = source_instance.__dict__
    attrs.pop("_sa_instance_state", None)

    return target_cls(**attrs)


def get_hydrated_base():
    return Base
