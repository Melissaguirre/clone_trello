from pydantic import BaseModel
from datetime import datetime 
from typing import Optional 


class CommentBase(BaseModel):
    id: str
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
    id : str


class CommentInDBBase(CommentBase):
    id : str 
    date_modified : datetime 

    class Config:
        orm_mode = True


class Comment(CommentInDBBase):
    ...