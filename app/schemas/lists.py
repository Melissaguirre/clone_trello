from pydantic import BaseModel 

class ListBase(BaseModel):
    list_name : str 
    order : int 
    workspaceID : str 

class ListCreate(ListBase):
    listID : str


class ListUpdate(BaseModel):
    list_name : str 
    order : int

class ReadList(ListBase):
    listID : str 

class ListInDBBase(ListBase):
    ListID : str 

    class Config:
        orm_mode = True

class Lists(ListInDBBase):
    ...