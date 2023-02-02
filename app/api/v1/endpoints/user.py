from fastapi import APIRouter, HTTPException, Response, status, Request
from fastapi.responses import JSONResponse
from typing import List, Any, Union
from app import schemas, crud, models
from app.models.users import Users

user = APIRouter()

# read all user
@user.get("/user", response_model=List[schemas.ReadUser], tags=["User"])
async def read_users(skip: int = 0, limit: int = 100) -> Any:
    return await crud.users.get_all(skip=skip, limit=limit)


# read by userID
@user.get("/user/{id}", response_model=schemas.User, tags=["User"])
async def get_user(*, id: str) -> Any:
    user = await crud.users.get(id=id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User is not found")
    return user


# create user
@user.post("/user", response_model=schemas.User, tags=["User"])
async def create_user(*, user_in: schemas.UserCreate) -> Any:
    user = await crud.users.create(obj_in=user_in)
    if not user:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN,
            content={"detail":"the user with this id already exists"})
    return user


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
