from fastapi import APIRouter, FastAPI, HTTPException, Response, status, Request
from fastapi.responses import JSONResponse
from typing import List, Any, Union
from app import schemas, crud, models
from app.models.users import Users
import tortoise 

user = APIRouter()


# read all user
@user.get("/user", response_model=List[schemas.ReadUser], tags=["User"])
async def read_users(skip: int = 0, limit: int = 100) -> Any:
    return await crud.users.get_all(skip=skip, limit=limit)


# read by userID
@user.get("/user/{id}", response_model=schemas.User, tags=["User"])
async def get_user(*, id: str) -> Any:
    try:
        return await crud.users.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User is not found")


# create user
@user.post("/user", response_model=schemas.BaseUser, tags=["User"])
async def create_user(*, user_in: schemas.UserCreate) -> Any:
    try:
        return await crud.users.create(obj_in=user_in)  
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="The user with this id already exists.")  


# update user
@user.put("/user/{id}", tags=["User"])
async def update_user(*, id: str, user_in: schemas.UserUpdate) -> Any:
    user = await crud.users.update(id=id, obj_in=user_in)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User is not found")
    return user
    

# delete user
@user.delete("/user/{id}", tags=["User"])
async def delete_user(*, id: str) -> Any:
    user = await crud.users.remove(id=id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User is not found")
    return {"message": "Successfully deleted"}
