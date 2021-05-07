from blog.article.views import article
from blog.report.views import report
from blog.user.views import user
from flask import (
    Flask,
    request
)


# app = Flask(__name__)
#
#
# @app.route("/", methods=["GET", "POST"])
# def index():
#     return f'This is a {request.method} '

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(report)
    app.register_blueprint(article)
