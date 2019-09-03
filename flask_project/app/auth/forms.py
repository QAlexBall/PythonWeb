""" web forms """
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo  # , Regexp
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    """ login form """
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remeber_me = BooleanField(('Keep me login'))
    submit = SubmitField('Log In')


class RegistrationForm(FlaskForm):
    """ register form """
    telephone = StringField(
        'Telephone Number',
        validators=[DataRequired(), Length(11, 11)])
    email = StringField(
        'Email',
        validators=[DataRequired(), Length(1, 64), Email()])
    username = StringField(
        'Username',
        validators=[DataRequired()])
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            EqualTo('password2', 'Passwords must match.')])
    password2 = PasswordField(
        'Confirm Password',
        validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        """ validate_email """
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        """ validate_username """
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username already in use.')
