from pydantic import BaseModel 
from typing import Optional
from uuid import UUID

class ListBase(BaseModel):
    list_id : Optional[UUID]
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
    list_id : Optional[UUID]

    class Config:
        orm_mode = True


class Lists(ListInDBBase):
    ...