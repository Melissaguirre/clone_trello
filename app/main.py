from .core.config import settings

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.api_v1 import router

from .database.db import init_db


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    init_db(app)