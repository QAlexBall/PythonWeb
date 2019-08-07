from flask import Flask, render_template, request, redirect, url_for, session
import config
from models import User
from extensions import db
from decorators import login_required

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)



@app.route('/')
@login_required
def index():
    return render_template('index.html')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        telephone = request.form.get('telephone')
        password = request. form.get('password')
        user = User.query.filter(User.telephone == telephone,
                                 User.password == password, ).first()
        if user:
            session['user_id'] = user.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            return render_template('login.html', message={'error: phone or password error!'})

@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        telephone = request.form.get('telephone')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return 'telephone exist! Please change.'
        else:
            if password1 != password2:
                return 'password confirm error!'
            else:
                user = User(telephone=telephone,
                            username=username,
                            password=password1)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('login'))

@app.route('/logout/')
def logout():
    session.pop('user_id')
    # del session['user_id']
    # session.clear()
    return redirect(url_for('login'))

@app.route('/question/')
@login_required
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        pass

@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user' : user}
    return {}

if __name__ == '__main__':
    app.run(debug=True)
