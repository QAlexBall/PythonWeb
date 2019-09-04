""" app/__init__.py"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_cors import CORS
from flask_misaka import Misaka
from celery import Celery
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate()
misaka = Misaka()
celery_app = Celery('tasks', broker='amqp://119.23.33.220:5672/', backend='amqp://119.23.33.220:5672/')
login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name='default'):
    """ create app """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    misaka.init_app(app)
    login_manager.init_app(app)
    CORS(app)
    celery_app = create_celery_app(app)
    # add router
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    from .email import email_bp as email_blueprint
    from .blog import blog as blog_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(email_blueprint)
    app.register_blueprint(blog_blueprint)
    return app


def create_celery_app(app=None):
    """ create celery app """
    app = app or create_app('default')
    celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):
        """ Context Task """
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return super(TaskBase, self).__call__(*args, **kwargs)
    celery.Task = ContextTask
    return celery
