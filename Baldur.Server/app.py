from flask import Flask
from waitress import serve
from models import *
import settings.database

from controllers.app_filters import bp as filters
from controllers.index_controller import ctrl as index_ctrl
from controllers.graphql_controller import ctrl as graphql_ctrl


app = Flask(__name__)

app.register_blueprint(filters)
app.register_blueprint(index_ctrl)
app.register_blueprint(graphql_ctrl)


if __name__ == "__main__":
    if app.env == "production":
        serve(app, port=5000)
    else:
        app.run()
