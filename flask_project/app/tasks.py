'''
Celery Tasks
'''
from app import celery_app as celery


@celery.task
def send_async_email(email_data):
    '''
    Background task to send an email with Flask-Mail.
    '''
    print(email_data)
    return email_data
