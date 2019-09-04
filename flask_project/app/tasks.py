''' Celery Tasks '''
import sys
sys.path.append('..')
from flasky import app
from flask_mail import Message
from app import create_celery_app, mail
celery = create_celery_app()


@celery.task
def send_async_email(email_data):
    ''' Background task to send an email with Flask-Mail. '''
    msg = Message(email_data['subject'],
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email_data['to']])
    msg.body = email_data['body']
    mail.send(msg)
