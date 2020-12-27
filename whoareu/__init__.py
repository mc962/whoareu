from flask import Flask

from whoareu.blueprints import register_blueprints
from whoareu.configuration import load_env, register_app_settings


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(load_env())

    register_app_settings(app)
    register_blueprints(app)

    return app
