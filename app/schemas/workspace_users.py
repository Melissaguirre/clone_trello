from pydantic import BaseModel 
from datetime import datetime

class WorkspaceUserBase(BaseModel):
    workspaceID : str
    userID : str
    date : datetime

class WorkspaceUserCreate(WorkspaceUserBase):
    ...

class WorkspaceUserUpdate(BaseModel):
    date : datetime 

class WorkspaceUserRead(WorkspaceUserBase):
    ...

class WorkspaceUserInDBBase(WorkspaceUserBase):
    workspaceID : str 

    class Config:
        orm_mode = True

class WorkspaceUser(WorkspaceUserInDBBase):
    ...