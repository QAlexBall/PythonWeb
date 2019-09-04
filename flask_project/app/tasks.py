'''
Celery Tasks
'''
<<<<<<< HEAD
from app import celery_app as celery

=======
import app
from app import create_celery_app, mail
from flask_mail import Message
celery = create_celery_app()
>>>>>>> 5d07f699ba4ff9a169470eea8bbf69c6520df74c


@celery.task
def send_async_email(email_data):
    ''' Background task to send an email with Flask-Mail. '''
    msg = Message(email_data['subject'],
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email_data['to']])
    msg.body = email_data['body']
    mail.send(msg)
