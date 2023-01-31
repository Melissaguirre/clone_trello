from fastapi import APIRouter, HTTPException 
from fastapi.encoders import jsonable_encoder
from typing import List, Any
from app import crud, models, schemas

workspace = APIRouter()

#read all workspeaces
@workspace.get("/workspace", response_model=List[schemas.ReadWorkspace], tags=["Workspace"])
async def get_workspaces(skip: int = 0, limit: int = 100) -> Any:
    return await crud.workpaces.get_all(skip=skip, limit=limit)

#read workspaces by workspaceID
@workspace.get("/workspace/{workspaceID}", response_model=schemas.Workspace, tags=["Workspace"])
async def get_workspaces(workspaceID: str)-> Any:
    workspace = await crud.workpaces.get(workspaceID=workspaceID)
    if not workspace:
        raise HTTPException(status_code=404, detail="Workspace is not found")
    return workspace 

#create workspace
@workspace.post("/workspace",response_model=schemas.Workspace, tags=["Workspace"])
async def create_workspace(workspace_in: schemas.WorkspaceCreate) -> Any:
    workspace = await crud.workpaces.create(obj_in=workspace_in)
    return workspace

#update workspace
@workspace.put("/workspace/{workspaceID}",response_model=schemas.Workspace, tags=["Workspace"])
async def update_workspace(workspace_in: schemas.WorkspaceUpdate, workspaceID: str)-> Any:
    workspace = await crud.workpaces.update(workspaceID=workspaceID, obj_in=workspace_in)
    if not workspace:
        raise HTTPException(
            status_code=404, 
            detail = "Workspace is not found")
    return workspace 

#delete workspace
@workspace.delete("/workspace/{workspaceID}", tags=["Workspace"])
async def delete_workspace(workspaceID: str) -> Any:
    workspace = await crud.workpaces.remove(workspaceID=workspaceID)
    if not workspace:
        raise HTTPException(
            status_code = 404, 
            detail = "Workspace is not found")
    return {"message" : "Successfully deleted"}

