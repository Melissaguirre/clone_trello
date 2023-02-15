from pydantic import BaseModel
from datetime import datetime 
from typing import Optional
from uuid import UUID 


class CommentBase(BaseModel):
    id : Optional[UUID]
    activity : Optional[bool]  
    comment_content : Optional[str] 
    date_created : datetime 
    date_modified : datetime  
    card_id: Optional[str]  
    user_id : Optional[str] 


class CommentCreate(CommentBase):
   ...


class CommentUpdate(BaseModel):
    activity : Optional[bool]  
    comment_content : Optional[str] 
    date_modified : datetime  


class ReadComment(CommentBase): 
    id : Optional[UUID]


class CommentInDBBase(CommentBase):
    id : Optional[UUID] 
    date_modified : datetime 

    class Config:
        orm_mode = True


class Comment(CommentInDBBase):
    ...