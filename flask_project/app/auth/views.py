'''
Auth Page
'''
from flask import render_template
from . import auth


@auth.route('/login/')
def login():
    '''
    login
    '''
    return render_template('index.html')
