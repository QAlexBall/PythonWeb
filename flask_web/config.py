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


import os
import pymysql
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '*****'
    MAIL_SERVER = 'smtp.domain.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = '*****'
    MAIL_PASSWORD = '*****'
    FLASKY_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    FLASKY_MAIL_SENDER = '*****'
    FLASKY_ADMIN = '*****'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = '*****'

config = {
    'development':DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,

    'default':DevelopmentConfig
}
