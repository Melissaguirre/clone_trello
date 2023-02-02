from pydantic import BaseModel 
from typing import Optional

class ListBase(BaseModel):
    list_id : str 
    list_name : Optional[str] 
    order : Optional[int] 
    workspace_id : Optional[str] 

class ListCreate(ListBase):
    ...

class ListUpdate(BaseModel):
    list_name : Optional[str] 
    order : Optional[int]

class ReadList(ListBase):
    ...

class ListInDBBase(ListBase):
    list_id : str 

    class Config:
        orm_mode = True

class Lists(ListInDBBase):
    ...