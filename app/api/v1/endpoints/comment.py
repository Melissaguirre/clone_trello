from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List , Any
from app import schemas, models, crud
import tortoise 

router = APIRouter()


#read comment 
@router.get("", response_model=List[schemas.Comment])
async def get_comments(skip: int = 0, limit: int = 100) -> Any:
    return await crud.comments.get_all(skip=skip, limit=limit)


#count comments
@router.get("/count")
async def count_comments(self, *, skip: int = 0, limit: int = 100):
    comment = await crud.comments.get_all(skip=skip, limit=limit)
    return {"number of comments": comment}


#read by id
@router.get("/{id}", response_model=schemas.Comment)
async def get_comment(id: str) -> Any:
    try:
        return await crud.comments.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment is not found")


#create comment
@router.post("", response_model=schemas.Comment)
async def create_comment(comment_in: schemas.CommentCreate) -> Any:
    try:
        return await crud.comments.create(obj_in=comment_in)
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Comment is not found")


#update comment
@router.put("/{id}", response_model=schemas.Comment)
async def update_comment(id: str, comment_in: schemas.CommentUpdate) -> Any:
    comment = await crud.comments.update(id=id, obj_in=comment_in)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment is not found")
    return comment


#delete comment
@router.delete("/{id}")
async def delete_comment(id: str) -> Any:
    comment = await crud.comments.remove(id=id)
    if not comment:
        raise HTTPException(
            status_code=404,
            detail="Comment is not found")
    return {"message" : "Successfully deleted"}
    