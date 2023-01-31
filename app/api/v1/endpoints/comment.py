from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List , Any
from app import schemas, models, crud

comment = APIRouter()

#read comment 
@comment.get("/comment", response_model=List[schemas.Comment], tags=["Comment"])
async def get_comments(skip: int = 0, limit: int = 100) -> Any:
    return await crud.comments.get_all(skip=skip, limit=limit)

@comment.get("/comment/{commentID}", response_model=schemas.Comment, tags=["Comment"])
async def get_comment(commentID: str) -> Any:
    return await crud.comments.get(commentID=commentID)

@comment.post("/comment", response_model=schemas.Comment, tags=["Comment"])
async def create_comment(comment_in: schemas.CommentCreate) -> Any:
    comment = await crud.comments.create(obj_in=comment_in)
    return comment

@comment.put("/comment/{commentID}", response_model=schemas.Comment, tags=["Comment"])
async def update_comment(commentID: str, comment_in: schemas.CommentUpdate) -> Any:
    comment = await crud.comments.update(commentID=commentID, obj_in=comment_in)
    return comment

@comment.delete("/comment/{commentID}", tags=["Comment"])
async def delete_comment(commentID: str) -> Any:
    comment = await crud.comments.delete(commentID=commentID)
    return {"message" : "Successfully deleted"}
    