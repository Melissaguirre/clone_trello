from datetime import timedelta
from typing import Any 
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordRequestForm
from app import crud, models, schemas 
from app.core import security
from app.core.config import settings
from app.api import deps


login = APIRouter()


@login.post("/login/access-token", response_model=schemas.Token) 
async def login_access_token(form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    user = await crud.users.authenticate(id=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect id or password")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    return {
        "access_token": security.create_access_token(user.id, expires_delta=access_token_expires),
        "token_type": "bearer",
    }

@login.post("/login/test-token", response_model=schemas.User)
async def token_current_user(current_user: models.Users = Depends(deps.get_current_user)) -> Any:
    return current_user