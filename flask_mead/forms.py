from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email


class RegisterForm(FlaskForm):
    name = StringField("Your Name", validators=[DataRequired()])
    email = EmailField("Your email", [DataRequired(), Email()])
    password = PasswordField("Your password", validators=[DataRequired()])
    password_confirm = PasswordField(
        "Repeat your password", validators=[DataRequired()]
    )


class LoginForm(FlaskForm):
    email = EmailField("Your email", [DataRequired(), Email()])
    password = PasswordField("Your password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
