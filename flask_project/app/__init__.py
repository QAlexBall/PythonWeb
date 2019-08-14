'''
app/__init__.py 应用包的构造文件
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import config
from .main import main as main_blueprint

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
migrate = Migrate()


def create_app(config_name):
    '''
    create_app
    '''
    app = Flask(__name__)
    app.config.from_object(config['config_name'])
    config['config_name'].init_app(app)
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    # 添加路由和自定义的错误页面
    app.register_blueprint(main_blueprint)
    return app
