""" web forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    """ login form """
    telephone = StringField('telephone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remeber_me = BooleanField(('Keep me login'))
    submit = SubmitField('Log In')
