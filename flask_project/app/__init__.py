'''
app/__init__.py 应用包的构造文件
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from celery import Celery
from config import config
from .main import main as main_blueprint
from .auth import auth as auth_blueprint

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate()
celery = Celery()


def create_app(config_name):
    '''
    create_app
    '''
    app = Flask(__name__)
    #  app.config.from_object(config['config_name'])
    app.config.from_object(config[str(config_name)])
    config[str(config_name)].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    celery.conf.update(app.config)
    print('register_blueprint', auth_blueprint)
    # add router
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    return app
