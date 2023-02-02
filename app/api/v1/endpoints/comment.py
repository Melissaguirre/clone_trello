from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List , Any
from app import schemas, models, crud

comment = APIRouter()

#read comment 
@comment.get("/comment", response_model=List[schemas.Comment], tags=["Comment"])
async def get_comments(skip: int = 0, limit: int = 100) -> Any:
    return await crud.comments.get_all(skip=skip, limit=limit)

#read by id
@comment.get("/comment/{id}", response_model=schemas.Comment, tags=["Comment"])
async def get_comment(id: str) -> Any:
    return await crud.comments.get(id=id)

#create comment
@comment.post("/comment", response_model=schemas.Comment, tags=["Comment"])
async def create_comment(comment_in: schemas.CommentCreate) -> Any:
    comment = await crud.comments.create(obj_in=comment_in)
    return comment

#update comment
@comment.put("/comment/{id}", response_model=schemas.Comment, tags=["Comment"])
async def update_comment(id: str, comment_in: schemas.CommentUpdate) -> Any:
    comment = await crud.comments.update(id=id, obj_in=comment_in)
    return comment

#delete comment
@comment.delete("/comment/{id}", tags=["Comment"])
async def delete_comment(id: str) -> Any:
    comment = await crud.comments.remove(id=id)
    return {"message" : "Successfully deleted"}
    