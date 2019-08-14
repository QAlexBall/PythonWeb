#config.py 应用的配置
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
    'development' : DevelopmentConfig,
    'testing' : TestingConfig,
    'production' : ProductionConfig,

    'default' : DevelopmentConfig
}
