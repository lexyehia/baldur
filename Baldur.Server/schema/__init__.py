from models import *  # Needed to pre-load models

from graphene import Schema
from .root_query import RootQuery
from .root_mutation import RootMutation

schema = Schema(query=RootQuery, mutation=RootMutation)
