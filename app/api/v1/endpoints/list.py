from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Any 
from app import schemas, models, crud
import tortoise

router = APIRouter()


#read list 
@router.get("", response_model=List[schemas.ReadList])
async def get_lists(skip: int = 0, limit: int = 100) -> Any:
    return await crud.lists.get_all(skip=skip, limit=limit)


#count lists 
@router.get("/count")
async def count_users(skip: int = 0, limit: int = 100) -> Any:
    lists = await crud.lists.count_all(skip=skip, limit=limit)
    return {"number of lists": lists}


#filter by name list
@router.get("/{list_name}", response_model=schemas.BaseUser)
async def get_user_by_name(list_name : str) -> Any:
    return await crud.users.filter_name_user(list_name=list_name)


#read list by listID
@router.get("/{list_id}", response_model=schemas.Lists)
async def get_list(*, list_id: str) -> Any:
    try:
        return await crud.lists.get_by_id(list_id=list_id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="List is not found")


#create list
@router.post("", response_model=schemas.Lists) 
async def create_list(list_in: schemas.ListCreate) -> Any:
    try:
        return await crud.lists.create(obj_in=list_in)
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The list with this list_id already exists.")
 

#update list
@router.put("/{list_id}", response_model=schemas.Lists)
async def update_list(*, list_id: str, list_in: schemas.ListUpdate) -> Any:
    lists = await crud.lists.update(list_id=list_id, obj_in=list_in)
    if not lists:
        raise HTTPException(
            status_code=404, 
            detail="List is not found")
    return lists

#delete list 
@router.delete("/{id_list}")
async def delete_list(*, id_list: str) -> Any:
    lists = await crud.lists.remove(id_list=id_list)
    if not lists:
        raise HTTPException(
            status_code=404, 
            detail="List is not found")
    return {"message" : "Successfully deleted"}
