#app/main/__init__.py 创建主蓝本
from flask import Blueprint

main = Blueprint('main', __name__)
from . import views, errors
