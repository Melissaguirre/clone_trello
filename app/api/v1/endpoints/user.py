from fastapi import APIRouter, HTTPException, Response
from fastapi.encoders import jsonable_encoder
from typing import List, Any, Union
from app import schemas, crud
from app.models.users import Users

user = APIRouter()

#read all user
@user.get("/user", response_model=List[schemas.ReadUser], tags=["User"])
async def read_users(skip: int = 0, limit: int = 100) -> Any:
    return await crud.users.get_all(skip=skip, limit=limit)


#read by userID
@user.get("/user/{userID}", response_model=schemas.User, tags = ["User"])
async def get_user(userID : str)  -> Any:
    user = await crud.users.get(userID=userID)
    if not user:
        raise HTTPException(
            status_code=404, 
            detail="User is not found")
    return user 

#create user 
@user.post("/user", response_model=schemas.User, tags = ["User"])
async def create_user(*, user_in: schemas.UserCreate) -> Any:
    user = await crud.users.create(obj_in=user_in)
    if user:
        raise HTTPException(
            status_code=400, 
            detail="The user already exists in the system.")
    return user 


#update user 
@user.put("/user/{userID}", tags=["User"])
async def update_user(*, userID: str, user_in: schemas.UserUpdate) -> Any:
    user = await crud.users.update(id=userID, obj_in=user_in)
    if not user:
        raise HTTPException(
            status_code=404, 
            detail="User is not found")
    return await Users.get(id=userID)

#delete user
@user.delete("/user/{userID}", tags = ["User"])
async def delete_user(*, userID : str) -> Any:
    user = await crud.users.remove(userID=userID)
    if not user:
        raise HTTPException(
            status_code=404, 
            detail = "User is not found")
    return {"message" : "Successfully deleted"}