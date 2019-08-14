'''
Extentions
'''
from flask_sqlalchemy import SQLAlchemy
from celery import Celery


db = SQLAlchemy()
CELERY = Celery()
