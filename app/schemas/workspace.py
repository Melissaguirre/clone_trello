from pydantic import BaseModel 
from typing import Optional


class WorkspaceBase(BaseModel):
    id : str 
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
    id : str 

    class Config:
        orm_mode = True


class Workspace(WorkspaceInDBBase):
    ...