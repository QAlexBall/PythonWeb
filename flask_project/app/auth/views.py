"""
Auth Page
"""
from flask import render_template, request, url_for, flash, redirect
from flask_login import login_user, logout_user
from . import auth
from .forms import LoginForm
from ..models import User


@auth.route('/')
def index():
    """ index """
    return "auth index, hello"


@auth.route('/login/', methods=['GET', 'POST'])
def login():
    """ login """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(telephone=form.telephone.data).first()
        print(user)
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remeber_me.data)
            next_page = request.args.get('next')
            if next_page is None or not next_page.startswith('/'):
                next_page = url_for('main.index')
            return redirect(next_page)
        flash('Invalid username or password')
    return render_template('auth/login.html', form=form)


@auth.route('/logout/')
def logout():
    """ logout """
    logout_user()
    return redirect(url_for('auth.login'))
