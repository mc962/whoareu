from flask import Flask

from whoareu.blueprints import errors, landings


def register_error_handlers(app: Flask):
    app.register_error_handler(404, errors.page_not_found)
    app.register_error_handler(500, errors.internal_server_error)


def register_blueprints(app: Flask):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app

    register_error_handlers(app)
    app.register_blueprint(landings.blueprint)
