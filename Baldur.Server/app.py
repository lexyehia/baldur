from flask import Flask, escape, request
from controllers.index_controller import ctrl as index_ctrl

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "World")
    return f"Hello there {escape(name)}"

@app.route("/home", methods=["POST"])
def home():
    name = request.args.get("name")
    return "Got it"

app.register_blueprint(index_ctrl)


