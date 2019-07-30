from os import getenv
from flask import Flask, escape, request
from controllers.index_controller import ctrl as index_ctrl
from helpers.authenticator import create_token, verify_token
from flask_graphql import GraphQLView
from schemas import schema
from waitress import serve

app = Flask(__name__)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://localhost:4200'
    header['Access-Control-Allow-Headers'] = 'origin content-type'
    return response


@app.route("/")
def hello():
    token = create_token("bob@bob.com")
    return token


@app.route("/verify/<token>")
def verify(token):
    return verify_token(token)


@app.route("/home", methods=["POST"])
def home():
    name = request.args.get("name")
    return "Got it"

app.add_url_rule("/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True))


app.register_blueprint(index_ctrl)

if __name__ == "__main__":
    if getenv("ENV") == "Production":
        serve(app, port=5000)
    else:
        app.run()
