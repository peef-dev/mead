import os

from flask import Flask, g, render_template
from flask_login import current_user

from application.config import DATABASE_URI, SECRET_KEY
from application.extensions import db, login_manager, migrate
from application.views.auth import auth_bp
from application.views.index import index_bp

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def register_config(app):
    app.config["POSTS_PER_PAGE"] = 10
    app.config["SECRET_KEY"] = SECRET_KEY
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    app.config["UPLOAD_FOLDER"] = os.path.join(basedir, "uploads")


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db, compare_type=True)
    login_manager.init_app(app)


def register_blueprints(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")


def register_jinja_filters(app):
    app.jinja_env.filters["format_date_time"] = lambda date, format=None: date.strftime(
        format
    )
    app.jinja_env.globals["DEBUG"] = bool(os.environ.get("FLASK_DEBUG"))


def register_error_pages(app):
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(403)
    def access_error(e):
        return render_template("errors/403.html"), 403


def register_context(app):
    @app.before_request
    def add_user_to_globals():
        if current_user.is_authenticated:
            g.current_user = current_user
        else:
            g.current_user = None

    @app.context_processor
    def inject_current_user():
        return {"current_user": g.current_user}


def create_app():
    app = Flask(__name__)
    register_config(app)
    register_extensions(app)
    register_blueprints(app)
    register_jinja_filters(app)
    register_error_pages(app)
    register_context(app)
    return app
