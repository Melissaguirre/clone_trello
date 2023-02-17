import os 
import time 
from celery import Celery

broker_url = "amqp://user:mypass@localhost:5672//"
result_backend = "rpc://"

celery = Celery('celery', broker=broker_url, backend=result_backend)

@celery.task
def test_celery(name):
    time.sleep(10)
    return name.upper()