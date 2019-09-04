from app import create_celery_app
celery = create_celery_app()


@celery.task
def add(x, y):
    return x + y
