'''
from .extensions import email_bp
Flask Project Config
'''
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    '''
    Base Config
    '''
    SECRET_KEY = os.urandom(24)
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_PORT = 587
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    #  MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = '1301033476@qq.com'
    FLASKY_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    FLASKY_MAIL_SENDER = '*****'
    FLASKY_ADMIN = '*****'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''
    Development Config
    '''
    DEBUG = False
    # db config 
    USERNAME = 'root'
    PASSWORD = 'zhuderen'
    HOSTNAME = '127.0.0.1'
    PORT = '3306'
    DATABASE = 'flask_project'
    DB_URI = 'mysql+mysqldb://{}:{}@{}:{}/{}'.format(
        USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    SQLALCHEMY_DATABASE_URI = DB_URI
    # celery
    CELERY_BROKER_URL = 'amqp://119.23.33.220:5672/'
    CELERY_RESULT_BACKEND = 'amqp://119.23.33.220:5672/'


class TestingConfig(Config):
    '''
    Testing Config
    '''
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or 'sqlite://'


class ProductionConfig(Config):
    '''
    Production Config
    '''
    SQLALCHEMY_DATABASE_URI = '*****'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
