from os import getenv
from flask import Flask, escape, request, g
from controllers.index_controller import ctrl as index_ctrl
from helpers.authenticator import create_token, verify_token
from flask_graphql import GraphQLView
from schemas import schema
from waitress import serve
from settings.database import Session
from models.user import User

app = Flask(__name__)

@app.before_request
def authenticate_token():
    user = None
    auth_token = request.headers.get("Authorization")
    user_id = verify_token(auth_token)

    if user_id is not None:
        session = Session()
        user = session.query(User).filter_by(email=user_id).first()

    g.user = user


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = 'http://localhost:8080'
    header['Access-Control-Allow-Headers'] = 'origin content-type'
    return response


@app.route("/")
def hello():
    token = create_token("bob@rae.com")
    return token


@app.route("/verify_token")
def verify():
    token = request.headers.get("Authorization")
    return verify_token(token)


app.add_url_rule(
    "/graphql", 
    view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
)

app.register_blueprint(index_ctrl)

if __name__ == "__main__":
    if getenv("ENV") == "Production":
        serve(app, port=5000)
    else:
        app.run()
