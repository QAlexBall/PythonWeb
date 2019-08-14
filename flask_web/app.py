'''
Flask main web page
'''
from flask import Flask, redirect, render_template, request, session, url_for
from celery import Celery
import config
from decorators import login_required
from extensions import db
<<<<<<< Updated upstream
from models import User
from bp_apps.bp_mail import mail
from bp_apps.bp_test import test_blue_print
=======
from models import User, Question
>>>>>>> Stashed changes

APP = Flask(__name__)
APP.config.from_object(config)
CELERY = Celery(APP.name, broker=APP.config['CELERY_BROKER_URL'])
CELERY.conf.update(APP.config)
APP.register_blueprint(test_blue_print.BP)
APP.register_blueprint(mail.BP)
db.init_app(APP)


@APP.route('/')
@login_required
def index():
    '''
    index
    '''
    message = {}
    message['questions'] = Question.query.order_by(Question.id)
    print(message)
    return render_template('index.html', message)


@APP.route('/login/', methods=['GET', 'POST'])
def login():
    '''
    login
    '''
    if request.method == 'GET':
        return render_template('login.html')
    telephone = request.form.get('telephone')
    password = request. form.get('password')
    user = User.query.filter(User.telephone == telephone,
                             User.password == password, ).first()
    if user:
        session['user_id'] = user.id
        session.permanent = True
        return redirect(url_for('index'))
    return render_template('login.html',
                           message={'error: phone or password error!'})


@APP.route('/register/', methods=['GET', 'POST'])
def register():
    '''
    register
    '''
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
    return redirect(url_for('login'))


@APP.route('/logout/')
def logout():
    '''
    logout
    '''
    session.pop('user_id')
    # del session['user_id']
    # session.clear()
    return redirect(url_for('login'))


@APP.route('/send_question/', methods=['GET', 'POST'])
@login_required
def send_question():
    '''
    send_question
    '''
    if request.method == 'GET':
        return render_template('send_question.html')
    # POST
    title = request.form.get('title')
    content = request.form.get('content')
    question = Question(title=title, content=content)
    db.session.add(question)
    db.session.commit()
    return redirect(url_for('index'))


@APP.context_processor
def my_context_processor():
    '''
    my_context_processor
    '''
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}


if __name__ == '__main__':
    APP.run(debug=True)
