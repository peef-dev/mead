# coding: utf-8

from application import app
from sqlalchemy import desc
from application.models.post_model import PostModel
from application.models.user_model import UserModel
from application.models.photo_model import PhotoModel
from application.tools.helpers import admin_required
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user


def _get_user(id):
	return UserModel.query.filter_by(id=id).first()


@app.route('/')
def home():
	return render_template('index/home.html', **locals())