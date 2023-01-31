from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List, Any 
from app import schemas, models, crud

lists = APIRouter()

#read list 
@lists.get("/list", response_model=List[schemas.ReadList], tags=["List"])
async def get_lists(skip: int = 0, limit: int = 100) -> Any:
    return await crud.lists.get_all(skip=skip, limit=limit)

#read list by listID
@lists.get("/list/{listID}", response_model=schemas.Lists, tags=["List"])
async def get_list(listID: str) -> Any:
    lists = await crud.lists.get(listID=listID)
    if not lists:
        raise HTTPException(
            status_code=404, 
            detail="List is not found")
    return lists

#create list
@lists.post("/list", response_model=schemas.Lists, tags=["List"]) 
async def create_list(list_in: schemas.ListCreate) -> Any:
    lists = await crud.lists.create(obj_in=list_in)
    return lists 

#update list
@lists.put("/list/{listID}", response_model=schemas.Lists, tags=["List"])
async def update_list(*, listID: str, list_in: schemas.ListUpdate) -> Any:
    lists = await crud.lists.update( listID=listID, obj_in=list_in)
    if not lists:
        raise HTTPException(
            status_code=404, 
            detail="List is not found")
    return lists

#delete list 
@lists.delete("/list/{listID}", tags=["List"])
async def delete_list(listID: str) -> Any:
    lists = await crud.lists.remove(listID=listID)
    if not lists:
        raise HTTPException(
            status_code=404, 
            detail="List is not found")
    return {"message" : "Successfully deleted"}
