# -*- coding: utf-8 -*-

import werkzeug
from application import app
from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, current_user, login_required, logout_user
from application.models.user_model import UserModel
from application.tools.helpers import user_exist, username_exist, admin_required
from application import login_manager


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = UserModel.query.filter(UserModel.username == request.form['username']).one()

        if werkzeug.security.check_password_hash(str(user.password), request.form['password']):
            login_user(user, remember=True, force=True)
            return redirect(url_for('home'))
        else:
            flash('Your credentials are incorrects!')
            return redirect(url_for('login'))
    return render_template('user/login.html', **locals())


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = UserModel()

        if request.form['password'] == request.form['password_confirm']:
            data = {
                'username': request.form['username'],
                'password': request.form['password'],
                'cgu_accepted': request.form['cgu_accepted'],
                'is_admin': False
            }

            if not user_exist():
                data['is_admin'] = True

            if not username_exist(request.form['username']):
                this_user = user.create(data=data)
                login_user(this_user, remember=True, force=True)
                flash('Your account has been created successfully!')
                return redirect(url_for('home'))
            else:
                flash("This username already exists")
                return redirect(url_for('register'))
        else:
            flash("The passwords does not match")
            return redirect(url_for('register'))

    return render_template('user/register.html', **locals())


@app.route('/users')
@login_required
@admin_required
def list_users():
    users = UserModel.query().order(UserModel.created_at)
    return render_template('user/list_users.html', **locals())
