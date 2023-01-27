from pydantic import BaseModel
from datetime import datetime 

class CommentBase(BaseModel):
    activity : bool 
    comment_content : str 
    date_create : datetime 
    date_modified : datetime 
    userID : str  
    cardID : str 

class CommentCreate(CommentBase):
    commentID : str

class CommentUpdate(BaseModel):
    activity : bool 
    comment_content : str 
    date_create : datetime  
    date_modified : datetime  

class ReadComment(CommentBase): 
    commentID : str

class CommentInDBBase(CommentBase):
    commentID : str 

    class Config:
        orm_mode = True

class Comment(CommentInDBBase):
    ...