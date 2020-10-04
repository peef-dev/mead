# coding: utf-8

import re
import string
import random
from application import app
from application.models.user_model import UserModel
from flask_login import current_user
from functools import wraps
from flask import redirect, url_for

def user_exist():
    if len(UserModel.query.all()) < 1:
        return False
    else:
        return True

def username_exist(name):
    if UserModel.query.filter(UserModel.username==name).count() == 0:
        return False
    else:
        return True

def get_code():
    """Generates an ASCII code of 5 character radomly"""
    size = 5
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))


def admin_required(func):
    @wraps(func)
    def connect_user_admin(*arg, **kwargs):
        if current_user.is_authenticated and not current_user.is_admin:
            return redirect(url_for("home"))
        return func(*arg, **kwargs)
    return connect_user_admin
