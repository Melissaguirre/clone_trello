import tortoise 

from typing import List, Any, Union

from uuid import UUID

from fastapi import APIRouter, FastAPI, HTTPException, Response, status, Request
from fastapi.responses import JSONResponse

from app import schemas, crud, models
from app.models.users import Users
from app.worker.celery_app import test_celery

from firebase_admin import auth


router = APIRouter()


#count users 
@router.get("/count")
async def count_users(skip: int = 0, limit: int = 100) -> Any:
    return await crud.users.count_all(skip=skip, limit=limit)


# read all user
@router.get("", response_model=List[schemas.ReadUser])
async def read_users(skip: int = 0, limit: int = 100) -> Any:
    user = await crud.users.get_all(skip=skip, limit=limit)
    return user


#filter by name
@router.get("/filter/{first_name}", response_model=schemas.BaseUser)
async def get_user_by_name(first_name : str) -> Any:
    return await crud.users.filter_name_user(first_name=first_name)

@router.get("/test/{name}")
async def test(name: str):
    task = test_celery.delay(name)
    return {"message": "Name received", "id": f"{task}"}


# read by userID 
@router.get("/{id}", response_model=schemas.BaseUser)
async def get_by_id(id: str) -> Any:
    try:
        return await crud.users.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User is not found")


# create user
@router.post("", response_model=schemas.BaseUser)
async def create_user(*, user_in: schemas.UserCreate) -> Any:
    user = auth.create_user(email=user_in.email, password=user_in.password)
    user_in.id = user.uid
    try:
        return await crud.users.create(obj_in=user_in) 
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="The user with this id already exists.")  


# update user
@router.put("/{id}", response_model=schemas.BaseUser)
async def update_user(*, id: str, user_in: schemas.UserUpdate) -> Any:
    user = await crud.users.update(id=id, obj_in=user_in)
    print(id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User is not found")
    return user
    

# delete user
@router.delete("/{id}")
async def delete_user(*, id: str) -> Any:
    user = await crud.users.remove(id=id)
    if not user:
        raise HTTPException(
            status_code=404,
            detail="User is not found")
    return {"message": "Successfully deleted"}
