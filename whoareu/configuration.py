import os

from dotenv import load_dotenv
from flask import Flask

load_dotenv()


def load_env() -> object:
    env = os.environ.get('FLASK_ENV')

    if env == 'development':
        return Development
    elif env == 'production':
        return Production
    else:
        print(f"Unknown environment: {env}. Falling back to development environment.")
        return Development


def register_app_settings(app: Flask) -> Flask:
    app.url_map.strict_slashes = False

    return app


class Development:
    FLASK_ENV = 'development'

    SECRET_KEY = '79f7d5b1df5c2a08ec2d9d6b3051327c8a163264c5fcf859'


class Production:
    FLASK_ENV = 'production'

    SECRET_KEY = os.getenv('SECRET_KEY')
