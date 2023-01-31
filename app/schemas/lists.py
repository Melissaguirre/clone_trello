from pydantic import BaseModel 
from typing import Optional

class ListBase(BaseModel):
    listID : str 
    list_name : Optional[str] 
    order : Optional[int] 
    workspaceID : Optional[str] 

class ListCreate(ListBase):
    ...


class ListUpdate(BaseModel):
    list_name : Optional[str] 
    order : Optional[int]

class ReadList(ListBase):
    listID : str 

class ListInDBBase(ListBase):
    ListID : str 

    class Config:
        orm_mode = True

class Lists(ListInDBBase):
    ...