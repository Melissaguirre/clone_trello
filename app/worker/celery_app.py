import time 
import smtplib

from celery import Celery

from app.core.config import settings
from app.core.security import generate_token

broker_url = "amqp://user:mypass@rabbitmq:5672//"
result_backend = "rpc://"

celery = Celery('celery', broker=broker_url, backend=result_backend)


@celery.task
def test_celery(name):
    time.sleep(10)
    return name.upper()

@celery.task
def send_email(to: str):
    SUBJECT : str = "Verificación de registro."
    BODY: str = generate_token()
    message = f"Subject:{SUBJECT}\n\n{BODY}"
    encoded_message = message.encode('utf-8')
    
    smpt= smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT)
    smpt.starttls()
    smpt.login(settings.SMTP_USERNAME, settings.SMTP_PASSWORD)
    smpt.sendmail(settings.SMTP_USERNAME, to, encoded_message)