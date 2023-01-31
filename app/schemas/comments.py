from pydantic import BaseModel
from datetime import datetime 
from typing import Optional 

class CommentBase(BaseModel):
    commentID : str
    activity : Optional[bool]  
    comment_content : Optional[str] 
    date_create : datetime 
    date_modified : datetime 
    userID : str  
    cardID : str 

class CommentCreate(CommentBase):
   ...

class CommentUpdate(BaseModel):
    activity : Optional[bool]  
    comment_content : Optional[str] 
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