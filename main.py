from fastapi import FastAPI
from app.api.v1.endpoints.user import user
from app.api.v1.endpoints.card import card
from app.api.v1.endpoints.list import lists
from app.api.v1.endpoints.workspace import workspace
from app.api.v1.endpoints.comment import comment
from app.api.v1.endpoints.card_user import card_user
from app.api.v1.endpoints.workspace_user import workspace_user
from tortoise.contrib.fastapi import register_tortoise 
import uvicorn

app = FastAPI()

register_tortoise(
    app,
    db_url = 'mysql://usermysql:password@localhost:33066/proyecto',
    modules = {'models' : ['app.models']},
    generate_schemas = True
)

app.include_router(user)
app.include_router(workspace)
app.include_router(card)
app.include_router(lists)
app.include_router(comment)
app.include_router(workspace_user)
app.include_router(card_user)

