from pydantic import BaseModel 
from typing import Optional
from uuid import UUID

class WorkspaceBase(BaseModel):
    id : Optional[UUID]
    workspace_name : Optional[str] 
    background_imgURL : Optional[str] 
    starred : Optional[bool] 
    board_type : Optional[str] 


class WorkspaceCreate(WorkspaceBase):
    ...


class WorkspaceUpdate(BaseModel):
    workspace_name : Optional[str]
    background_imgURL : Optional[str] 
    starred : Optional[bool] 
    board_type : Optional[str] 


class ReadWorkspace(WorkspaceBase):
    ... 


class WorkspaceInDBBase(WorkspaceBase):
    id : Optional[UUID] 

    class Config:
        orm_mode = True


class Workspace(WorkspaceInDBBase):
    ...