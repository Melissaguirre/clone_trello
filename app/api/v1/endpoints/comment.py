from fastapi import APIRouter, HTTPException
from typing import List , Any
from app import schemas, models, crud


comment = APIRouter()

#read comment 
@comment.get("/comment", response_model = List[models.Comments], tags = ["Comment"])
async def get_comments(skip : int = 0, limit : int = 100) -> List[models.Comments]:
    return await crud.comments.get_all(skip = skip, limit = limit)

@comment.get("/comment/{commentID}", response_model =  schemas.Comment, tags = ["Comment"])
async def get_comment(commentID : str)-> models.Comments:
    return await crud.comments.get(commentID = commentID)

@comment.post("/comment/create", response_model = schemas.Comment, tags = ["Comment"])
async def create_comment(comment_in : schemas.CommentCreate)-> models.Comments:
    comment = await crud.comments.create(comment_in)
    return comment

@comment.put("/comment/{commentID}", response_model = schemas.Comment, tags = ["Comment"])
async def update_comment(commentID : str, comment : models.Comments, comment_in : schemas.CommentUpdate)->models.Comments:
    comment = await crud.comments.update(comment_in, commentID = commentID)
    return comment

@comment.remove("/comment/{commentID}", response_model = schemas.Comment, tags = ["Comment"])
async def delete_comment(commentID : str)-> models.Comments:
    comment = await crud.comments.delete(commentID = commentID)
    return comment 
    