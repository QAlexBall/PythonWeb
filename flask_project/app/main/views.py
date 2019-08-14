'''
Index Page '/'
'''
from flask import render_template
from . import main


@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    index
    '''
    return render_template('index.html')
