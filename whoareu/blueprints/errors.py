from flask import Blueprint, render_template

blueprint = Blueprint('errors', __name__)


@blueprint.errorhandler(404)
def page_not_found(_error):
    return render_template('404.html'), 404


@blueprint.errorhandler(500)
def internal_server_error(_error):
    return render_template('500.html'), 500
