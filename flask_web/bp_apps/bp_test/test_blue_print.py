from flask import Blueprint
BP = Blueprint('test', __name__, url_prefix='/test')

@BP.route('/')
def index():
    return 'test Blueprint'
