import logging

from fastapi import FastAPI

from tortoise import Tortoise 
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings
 

async def connectToDatabase():
    await Tortoise.init(
        db_url = 'mysql://root:@127.0.0.1:33066/proyecto',
        modules = {'models':['app.models']}
    )
    

def init_db(app:FastAPI):
    register_tortoise(
        app,
        db_url = settings.DB_URL,
        modules = {'models' : ['app.models']},
        generate_schemas = True
    )
    
async def generate_schemas():
       await Tortoise.init(
        db_url = settings.DB_URL,
        modules = {'models':['app.models']}
    )
       logging.info("Generating database schema via Tortoise...")
       await Tortoise.generate_schemas()
       await Tortoise.close_connections()