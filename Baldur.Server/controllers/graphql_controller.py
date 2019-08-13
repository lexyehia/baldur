from flask import Blueprint, request, jsonify, g, abort
from ariadne import graphql_sync
from schemas.schema import schema
from ariadne.constants import PLAYGROUND_HTML

ctrl = Blueprint("graphql", __name__, url_prefix="/graphql")


@ctrl.route("/", methods=["GET"])
def graphql_playground():
    if g.is_dev:
        return PLAYGROUND_HTML, 200

    return abort(404)


@ctrl.route("/", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=g.is_dev,
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
