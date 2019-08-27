"""
main app '/'
"""
from flask import render_template, request, session, url_for, redirect
from flask_login import login_required
from . import main
from .. import db
from ..models import User, Discuss
#  from ..decorators import login_required


@main.route('/test_json')
def test():
    """ test url """
    return {'test': 'test_message'}


@main.route('/')
@login_required
def index():
    """index"""
    message = {}
    message['discuss'] = Discuss.query.order_by(Discuss.id)
    print(message)
    return render_template('index.html', message=message)


@main.route('/login/', methods=['GET', 'POST'])
def login():
    """ login """
    if request.method == 'GET':
        return render_template('login.html')
    telephone = request.form.get('telephone')
    password = request.form.get('password')
    user = User.query.filter(User.telephone == telephone).first()
    if user and user.verify_password(password):
        session['user_id'] = user.id
        session.permanent = True
        return redirect(url_for('main.index'))

    return render_template('login.html',
                           message={'error: phone or password error!'})


@main.route('/register/', methods=['GET', 'POST'])
def register():
    """ register """
    if request.method == 'GET':
        return render_template('register.html')
    # POST
    telephone = request.form.get('telephone')
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    user = User.query.filter(User.telephone == telephone).first()
    if user:
        return 'telephone exist! Please change.'
    if password1 != password2:
        return 'password confirm error!'
    user = User(telephone=telephone,
                username=username,
                password=password1)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('main.login'))


@main.route('/old_logout/')
def old_logout():
    """ old logout """
    session.pop('user_id')
    # del session['user_id']
    # session.clear()
    return redirect(url_for('auth.login'))


@main.route('/send_discuss/', methods=['GET', 'POST'])
@login_required
def send_question():
    """ send question """
    if request.method == 'GET':
        return render_template('send_discuss.html')
    # POST
    title = request.form.get('title')
    content = request.form.get('content')
    discuss = Discuss(title=title, content=content)
    db.session.add(discuss)
    db.session.commit()
    return redirect(url_for('main.index'))


@main.context_processor
def my_context_processor():
    """ my_context_processor """
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}
