import time
from pyramid_celery import celery_app as app


@app.task
def my_task1(data):
    time.sleep(5)
    return 'ok'
