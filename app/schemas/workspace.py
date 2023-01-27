from pydantic import BaseModel 

class WorkspaceBase(BaseModel):
    workspaceID : str 
    workspace_name : str 
    background_imgURL : str 
    starred : bool 
    board_type : str 

class WorkspaceCreate(WorkspaceBase):
    ...

class WorkspaceUpdate(BaseModel):
    workspace_name : str 
    background_imgURL : str 
    starred : bool 
    board_type : str 

class ReadWorkspace(WorkspaceBase):
    ... 

class WorkspaceInDBBase(WorkspaceBase):
    workspaceID : str 

    class Config:
        orm_mode = True

class Workspace(WorkspaceInDBBase):
    ...