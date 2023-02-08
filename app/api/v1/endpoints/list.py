from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Any 
from app import schemas, models, crud
import tortoise

router = APIRouter()

#read list 
@router.get("/list", response_model=List[schemas.ReadList], tags=["List"])
async def get_lists(skip: int = 0, limit: int = 100) -> Any:
    return await crud.lists.get_all(skip=skip, limit=limit)

#read list by listID
@router.get("/list/{list_id}", response_model=schemas.Lists, tags=["List"])
async def get_list(*, list_id: str) -> Any:
    try:
        return await crud.lists.get_by_id(list_id=list_id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="List is not found")


#create list
@router.post("/list", response_model=schemas.Lists, tags=["List"]) 
async def create_list(list_in: schemas.ListCreate) -> Any:
    try:
        return await crud.lists.create(obj_in=list_in)
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The list with this list_id already exists.")
 

#update list
@router.put("/list/{list_id}", response_model=schemas.Lists, tags=["List"])
async def update_list(*, list_id: str, list_in: schemas.ListUpdate) -> Any:
    lists = await crud.lists.update(list_id=list_id, obj_in=list_in)
    if not lists:
        raise HTTPException(
            status_code=404, 
            detail="List is not found")
    return lists

#delete list 
@router.delete("/list/{id_list}", tags=["List"])
async def delete_list(*, id_list: str) -> Any:
    lists = await crud.lists.remove(id_list=id_list)
    if not lists:
        raise HTTPException(
            status_code=404, 
            detail="List is not found")
    return {"message" : "Successfully deleted"}
