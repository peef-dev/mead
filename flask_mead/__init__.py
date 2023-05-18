from flask import Blueprint, g, render_template
from flask_login import current_user

from flask_mead.extensions import db, login_manager, migrate
from flask_mead.views import IndexView, LoginView, LogoutView, RegisterView


class Mead:
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

        self.blueprint = Blueprint(
            "mead",
            __name__,
            template_folder="templates",
            static_folder="static",
            static_url_path="/flask_mead/static",
        )

    def register_extensions(self, app):
        db.init_app(app)
        migrate.init_app(app, db, compare_type=True)
        login_manager.init_app(app)

    def register_blueprints(self, app):
        self.blueprint.add_url_rule(
            "/", view_func=IndexView.as_view("index", template="index/home.html")
        )
        self.blueprint.add_url_rule(
            "/register",
            view_func=RegisterView.as_view("register", template="auth/register.html"),
            methods=["GET", "POST"],
        )
        self.blueprint.add_url_rule(
            "/login",
            view_func=LoginView.as_view("login", template="auth/login.html"),
            methods=["GET", "POST"],
        )
        self.blueprint.add_url_rule("/logout", view_func=LogoutView.as_view("logout"))
        app.register_blueprint(self.blueprint)

    def register_jinja_filters(self, app):
        app.jinja_env.filters[
            "format_date_time"
        ] = lambda date, format=None: date.strftime(format)

    def register_error_pages(self, app):
        @app.errorhandler(404)
        def page_not_found(e):
            return render_template("errors/404.html"), 404

        @app.errorhandler(403)
        def access_error(e):
            return render_template("errors/403.html"), 403

    def register_context(self, app):
        @app.before_request
        def add_user_to_globals():
            if current_user.is_authenticated:
                g.current_user = current_user
            else:
                g.current_user = None

        @app.context_processor
        def inject_current_user():
            return {"current_user": g.current_user}

    def init_app(self, app):
        self.register_extensions(app)
        self.register_blueprints(app)
        self.register_jinja_filters(app)
        self.register_error_pages(app)
        self.register_context(app)
