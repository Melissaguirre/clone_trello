from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List , Any
from app import schemas, models, crud
import tortoise 

comment = APIRouter()

#read comment 
@comment.get("/comment", response_model=List[schemas.Comment], tags=["Comment"])
async def get_comments(skip: int = 0, limit: int = 100) -> Any:
    return await crud.comments.get_all(skip=skip, limit=limit)

#read by id
@comment.get("/comment/{id}", response_model=schemas.Comment, tags=["Comment"])
async def get_comment(id: str) -> Any:
    try:
        return await crud.comments.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment is not found")

#create comment
@comment.post("/comment", response_model=schemas.Comment, tags=["Comment"])
async def create_comment(comment_in: schemas.CommentCreate) -> Any:
    try:
        return await crud.comments.create(obj_in=comment_in)
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Comment is not found")

#update comment
@comment.put("/comment/{id}", response_model=schemas.Comment, tags=["Comment"])
async def update_comment(id: str, comment_in: schemas.CommentUpdate) -> Any:
    comment = await crud.comments.update(id=id, obj_in=comment_in)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment is not found")
    return comment

#delete comment
@comment.delete("/comment/{id}", tags=["Comment"])
async def delete_comment(id: str) -> Any:
    comment = await crud.comments.remove(id=id)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment is not found")
    return {"message" : "Successfully deleted"}
    