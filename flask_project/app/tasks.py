""" Celery Tasks """
import sys
import time
import random
sys.path.append('..')
from flasky import app
from flask_mail import Message
from app import create_celery_app, mail
celery = create_celery_app(app)


@celery.task
def send_async_email(email_data):
    """ Background task to send an email with Flask-Mail. """
    print(" send async email to {}".format(email_data['to']))
    msg = Message(email_data['subject'],
                  sender=app.config['MAIL_DEFAULT_SENDER'],
                  recipients=[email_data['to']])
    msg.body = email_data['body']
    mail.send(msg)


@celery.task(bind=True)
def long_task_async(self):
    print(app.config)
    """ Background task that runs a long function with progress reports. """
    verb = ['Starting up', 'Booting', 'Repairing', 'Loading', 'Checking']
    adjective = ['master', 'radiant', 'silent', 'harmonic', 'fast']
    noun = ['solar array', 'particle reshape', 'cosmic ray', 'orbiter', 'bit']
    message = ''
    total = random.randint(10, 50)
    for i in range(total):
        if not message or random.random() < 0.25:
            message = '{0} {1} {2}...'.format(random.choice(verb),
                                              random.choice(adjective),
                                              random.choice(noun))
        self.update_state(state='PROGRESS',
                          meta={'current': i, 'total': total,
                                'status': message})
        time.sleep(random.randint(0, 1))
    return {'current': 100, 'total': 100, 'status': 'Task completed!',
            'result': 42}


@celery.task
def test_celery_changed():
    print("celery changed!")
    return 'changed?'
