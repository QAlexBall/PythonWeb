'''
Celery Tasks
'''
from app import create_celery_app, mail
celery = create_celery_app()


@celery.task
def send_async_email(email_data):
    '''
    Background task to send an email with Flask-Mail.
    '''
    mail.send(email_data)
