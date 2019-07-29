from flask import Flask, escape, request
from controllers.index_controller import ctrl as index_ctrl
from helpers.authenticator import create_token, verify_token

app = Flask(__name__)

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

app.register_blueprint(index_ctrl)


