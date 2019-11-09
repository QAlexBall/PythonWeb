"""
Auth Page
"""
from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, logout_user
from . import auth
from .forms import LoginForm, RegistrationForm
from ..models import User
from .. import db


@auth.route('/')
def index():
    """ index """
    return "auth index, hello"


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    """ login """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next_page = request.args.get('next')
            if next_page is None or not next_page.startswith('/'):
                next_page = url_for('main.index')
            return redirect(next_page)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/register/', methods=['GET', 'POST'])
def register():
    """ register """
    form = RegistrationForm()
    if form.validate_on_submit():
        # noinspection PyArgumentList
        user = User(telephone=form.telephone.data,
                    email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You can now login.')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/logout/')
def logout():
    """ logout """
    logout_user()
    return redirect(url_for('auth.login'))
