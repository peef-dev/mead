import os

import click
import psycopg2
from flask import Blueprint, g, render_template
from flask_login import current_user

from flask_mead.extensions import db, login_manager, migrate
from flask_mead.index import IndexView, LoginView, LogoutView, RegisterView
from flask_mead.models import User
from flask_mead.views import (
    ActionView,
    DetailView,
    FormView,
    Menu,
    MenuCategory,
    MenuItem,
)


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

        self.menu = Menu()

    def attach(self, name, view, url, **options):
        if isinstance(view, (FormView, DetailView, ActionView)):
            args = [name]
            kwargs = {}
            if hasattr(view, "model"):
                kwargs["model"] = view.model
            if hasattr(view, "template"):
                kwargs["template"] = view.template
            if isinstance(view, ActionView) and hasattr(view, "redirect_url"):
                kwargs["redirect_url"] = view.redirect_url

            self.blueprint.add_url_rule(
                url, view_func=view.as_view(*args, **kwargs), **options
            )
        else:
            self.blueprint.add_url_rule(url, view_func=view.as_view(name), **options)

    def register_extensions(self, app):
        db.init_app(app)
        migrate.init_app(app, db, compare_type=True)
        login_manager.init_app(app)

    def register_blueprints(self, app):
        index = IndexView(template="index/home.html")
        self.attach(name="index", view=index, url="/")

        register = RegisterView(template="auth/register.html", model=User)
        self.attach(name="register", view=register, url="/register")

        login = LoginView(template="auth/login.html", model=User)
        self.attach(name="login", view=login, url="/login", methods=["GET", "POST"])

        logout = LogoutView(redirect_url="mead.index")
        self.attach(name="logout", view=logout, url="/logout")

        app.register_blueprint(self.blueprint)

    def register_menu(self):
        painting = MenuItem("Paintings", link="www.menu.paintings", icon="fa-star")
        computer = MenuItem("Computers", link="www.menu.computers", icon="fa-star")
        products_menu = MenuCategory("Products", [painting, computer])

        self.menu.add_category(products_menu)
        return self.menu.build()

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
        def add_globals():
            g.menu = self.register_menu()
            if current_user.is_authenticated:
                g.current_user = current_user
            else:
                g.current_user = None

        @app.context_processor
        def inject_data():
            return {"current_user": g.current_user, "menuitems": g.menu}

    def register_commands(self, app):
        @app.cli.group()
        def mead():
            click.echo("Initialyzing your Flask-Mead")

        @mead.command("init")
        def init():
            db_name = os.getenv("DB_NAME")
            click.echo(f"Creating database {db_name}")
            conn = None
            try:
                conn = psycopg2.connect(
                    dbname="postgres",
                    user=os.getenv("DB_USER"),
                    host=os.getenv("DB_HOST"),
                    port=os.getenv("DB_PORT"),
                )
                conn.autocommit = True
                with conn.cursor() as cursor:
                    cursor.execute(f'CREATE DATABASE "{db_name}";')
                    cursor.execute("SELECT datname FROM pg_database")
                    databases = [db[0] for db in cursor]
                    if db_name in databases:
                        click.echo(f"Database '{db_name}' created successfully.")
                    else:
                        click.echo(f"Failed to create database '{db_name}'.")
            except psycopg2.errors.DuplicateDatabase:
                click.echo(f"Database '{db_name}' already exists.")
            finally:
                if conn:
                    conn.close()

    def init_app(self, app):
        self.register_extensions(app)
        self.register_blueprints(app)
        self.register_jinja_filters(app)
        self.register_error_pages(app)
        self.register_context(app)
        self.register_commands(app)
