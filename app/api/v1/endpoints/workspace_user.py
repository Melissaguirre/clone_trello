from fastapi import APIRouter, HTTPException
from typing import List, Any
from app import models, schemas, crud

workspace_user = APIRouter()

#read all workspace_user 
@workspace_user.get("/workspace_user", response_model = List[schemas.WorkspaceUserRead], tags = ["Workspace-User"])
async def read_workspace_users(skip : int = 0, limit : int =  100) -> Any:
    return await crud.workspace_user.get_all(skip = skip, limit = limit)

@workspace_user.get("/workspace_user/{workspaceID}", response_model = schemas.WorkspaceUser, tags = ["Workspace-User"])
async def get_workspace_user(workspaceID : str) -> Any:
    return await crud.workspace_user.get(workspaceID = workspaceID)

@workspace_user.post("/workspace_user/create", response_model = schemas.WorkspaceUser,  tags = ["Workspace-User"])
async def create_workspace_user(workspace_user_in : schemas.WorkspaceCreate) -> Any:
    workspace_user = await crud.workspace_user.create(workspace_user_in)
    return workspace_user

@workspace_user.put("/workspace_user/{workspaceID}", response_model = schemas.WorkspaceUser, tags = ["Workspace-User"])
async def update_workspace_user(workspaceID : str, workspace_user : models.WorkspaceUsers, workspace_user_in : schemas.WorkspaceUserCreate) -> Any:
    workspace_user = await crud.workspace_user.update(workspace_user_in, workspaceID = workspaceID)
    return workspace_user

@workspace_user.delete("/workspace_user/{workspaceID}", response_model = schemas.WorkspaceUser, tags = ["Workspace-User"])
async def delete_workspace_user(workspaceID : str) -> Any:
    workspace_user = await crud.workspace_user.remove(workspaceID = workspaceID)
    return workspace_user