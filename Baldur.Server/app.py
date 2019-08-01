from flask import Flask, escape, request, g
from flask_graphql import GraphQLView
from schemas import schema
from waitress import serve

from controllers.app_filters import bp as filters
from controllers.index_controller import ctrl as index_ctrl
from controllers.sessions_controller import ctrl as sessions_ctrl


app = Flask(__name__)


app.register_blueprint(filters)
app.register_blueprint(index_ctrl)
app.register_blueprint(sessions_ctrl)


app.add_url_rule(
    "/graphql",
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)


if __name__ == "__main__":
    if app.env == "Production":
        serve(app, port=5000)
    else:
        app.run()
