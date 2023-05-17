from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from sqlalchemy.exc import IntegrityError, NoResultFound
from werkzeug.security import check_password_hash

from application.extensions import db
from application.forms import LoginForm, RegisterForm
from application.services import RoleService, UserService

auth_bp = Blueprint("auth", __name__)
user = UserService(session=db.session)
role = RoleService(session=db.session)


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if len(role.get_all_roles()) == 0:
        role.create_first_roles()

    user_role = user.get_user_role("user")
    if len(user.get_all_users()) == 0:
        user_role = user.get_user_role("admin")

    if form.validate_on_submit():
        try:
            if form.password.data == form.password_confirm.data:
                user_id = user.create_user(
                    name=form.name.data,
                    email=form.email.data,
                    password=form.password.data,
                    role_id=user_role.id,
                )
                login_user(user.get_user_by_id(user_id), remember=True, force=True)
                flash("Your account has been successfully created!")
                return redirect(url_for("index.index"))
            else:
                flash("Password does not match!")
                return redirect(url_for("auth.register"))
        except IntegrityError:
            flash("The email you entered already exists!")
            return redirect(url_for("auth.register"))
    return render_template("auth/register.html", form=form)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        try:
            connected_user = user.get_user_by_email(form.email.data)
            check_password = check_password_hash(
                str(connected_user.password), form.password.data
            )
            if connected_user and check_password:
                login_user(connected_user, remember=form.remember_me.data, force=True)
                next = request.args.get("next")
                priority = url_for("index.index")
                return redirect(next or priority)
            else:
                flash("Your credentials are not correct!")
                return redirect(url_for("auth.login"))
        except (NoResultFound, AttributeError):
            flash("You don't have any account, please create one")
            return redirect(url_for("auth.register"))
    return render_template("auth/login.html", form=form)


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("index.index"))
