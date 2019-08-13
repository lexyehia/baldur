from ariadne import make_executable_schema, load_schema_from_path
from schemas.resolvers.user_resolvers import user_resolvers
from schemas.resolvers.transaction_resolvers import tranx_resolvers

resolvers = user_resolvers + tranx_resolvers

type_defs = load_schema_from_path("schemas")
schema = make_executable_schema(type_defs, resolvers)
