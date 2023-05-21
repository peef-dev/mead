from flask import flash, redirect, render_template, request, url_for
from flask_login import login_user, logout_user
from sqlalchemy.exc import IntegrityError, NoResultFound
from werkzeug.security import check_password_hash

from flask_mead.extensions import db
from flask_mead.forms import LoginForm, RegisterForm
from flask_mead.services import RoleService, UserService
from flask_mead.views import ActionView, DetailView, FormView

user = UserService(session=db.session)
role = RoleService(session=db.session)


class IndexView(DetailView):
    def __init__(self, template, model=None):
        super().__init__(template, model=None)

    def dispatch_request(self):
        return render_template(self.template)


class RegisterView(FormView):
    def __init__(self, template, model):
        super().__init__(template, model)

    def dispatch_request(self):
        form = RegisterForm()

        if len(role.get_all_roles()) == 0:
            role.create_first_roles()

        user_role = user.get_user_role("user")
        if len(user.get_all_users()) == 0:
            user_role = user.get_user_role("admin")

        if request.method == "POST":
            if form.validate_on_submit():
                try:
                    if form.password.data == form.password_confirm.data:
                        user_id = user.create_user(
                            name=form.name.data,
                            email=form.email.data,
                            password=form.password.data,
                            role_id=user_role.id,
                        )
                        login_user(
                            user.get_user_by_id(user_id), remember=True, force=True
                        )
                        flash("Your account has been successfully created!")
                        return redirect(url_for("mead.index"))
                    else:
                        flash("Password does not match!")
                        return redirect(url_for("mead.register"))
                except IntegrityError:
                    flash("The email you entered already exists!")
                    return redirect(url_for("mead.register"))
        return render_template(self.template, form=form)


class LoginView(FormView):
    def __init__(self, template, model):
        super().__init__(template, model)

    def dispatch_request(self):
        form = LoginForm()

        if request.method == "POST":
            if form.validate_on_submit():
                try:
                    connected_user = user.get_user_by_email(form.email.data)
                    check_password = check_password_hash(
                        str(connected_user.password), form.password.data
                    )
                    if connected_user and check_password:
                        login_user(
                            connected_user, remember=form.remember_me.data, force=True
                        )
                        next = request.args.get("next")
                        priority = url_for("mead.index")
                        return redirect(next or priority)
                    else:
                        flash("Your credentials are not correct!")
                        return redirect(url_for("mead.login"))
                except (NoResultFound, AttributeError):
                    flash("You don't have any account, please create one")
                    return redirect(url_for("mead.register"))
        return render_template(self.template, form=form)


class LogoutView(ActionView):
    def dispatch_request(self):
        logout_user()
        return redirect(url_for(self.redirect_url))
