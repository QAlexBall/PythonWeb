'''
web config
'''
import os

DEBUG = True

# session config
SECRET_KEY = os.urandom(24)

# db config
USERNAME = 'root'
PASSWORD = ''
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_web'
DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEDN = 'redis://localhost:6379/0'
# flask mail
MAIL_SERVER = 'stmp.googleemail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = 'flask@example.com'


