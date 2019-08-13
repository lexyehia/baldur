from ariadne import make_executable_schema, load_schema_from_path
from .user_resolvers import query as user_query, mutation as user_mutation
from .transaction_resolvers import query as tranx_query, mutation as tranx_mutation

resolvers = [
    user_query,
    tranx_query,
    user_mutation,
    tranx_mutation,
]

type_defs = load_schema_from_path("schemas")
schema = make_executable_schema(type_defs, resolvers)
