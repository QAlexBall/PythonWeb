<<<<<<< HEAD
from app import create_celery_app
celery = create_celery_app()


@celery.task
def add(x, y):
    return x + y
=======
from app import create_celery_app, mail
celery = create_celery_app()
>>>>>>> 5d07f699ba4ff9a169470eea8bbf69c6520df74c
