from pydantic import BaseModel 
from typing import Optional
from datetime import datetime
from uuid import UUID

class WorkspaceUserBase(BaseModel):
    id : Optional[UUID]
    workspace_id: Optional[str]
    user_id : Optional[str]
    date : datetime


class WorkspaceUserCreate(WorkspaceUserBase):
    ...


class WorkspaceUserUpdate(BaseModel):
    date : datetime 


class WorkspaceUserRead(WorkspaceUserBase):
    ...


class WorkspaceUserInDBBase(WorkspaceUserBase):
    id : Optional[UUID]

    class Config:
        orm_mode = True


class WorkspaceUser(WorkspaceUserInDBBase):
    ...