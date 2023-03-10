import secrets 

from typing import Any, Dict, List, Optional, Union
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, validator 


class Settings(BaseSettings):
    
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8 
    DB_URL: str = 'mysql://usermysql:password@mysql:33066/proyecto'
    
    #celery
    CELERY_BROKER_URL: str = 'amqp://user:mypass@rabbitmq:5672//'
    CELERY_RESULT_BACKEND: str = 'rpc://'
    
    #environments email
    SMTP_HOST: str = 'smtp.gmail.com'
    SMTP_PORT: int = 587
    SMTP_USERNAME: str = 'melissaguirre8@gmail.com'
    SMTP_PASSWORD: str = "fqasptonwjhhhdsh"

      
settings = Settings()