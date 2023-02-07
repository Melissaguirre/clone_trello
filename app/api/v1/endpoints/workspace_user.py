from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Any
from app import models, schemas, crud
import tortoise 

workspace_user = APIRouter()

#read all workspace_user 
@workspace_user.get("/workspace_user", response_model=List[schemas.WorkspaceUserRead], tags=["Workspace-User"])
async def read_workspace_users(skip: int = 0, limit: int =  100) -> Any:
    return await crud.workspace_user.get_all(skip=skip, limit=limit)

#get workspace user 
@workspace_user.get("/workspace_user/{id}", response_model=schemas.WorkspaceUser, tags=["Workspace-User"])
async def get_workspace_user(id : str) -> Any:
    try:
        return await crud.workspace_user.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Workspace user is not found.")

#create workspace user
@workspace_user.post("/workspace_user", response_model=schemas.WorkspaceUser, tags=["Workspace-User"])
async def create_workspace_user(workspace_user_in: schemas.WorkspaceUserCreate) -> Any:
    try:
        return await crud.workspace_user.create(obj_in=workspace_user_in)
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The workspace user with id already exists.")

#update workspace user
@workspace_user.put("/workspace_user/{id}", response_model=schemas.WorkspaceUser, tags=["Workspace-User"])
async def update_workspace_user(*, id: str, workspace_user_in: schemas.WorkspaceUserUpdate) -> Any:
    workspace_user = await crud.workspace_user.update(id=id, obj_in=workspace_user_in)
    if not workspace_user:
        raise HTTPException(
            status_code=404, 
            detail="Workspace user is not found.")
    return workspace_user

#delete workspace user
@workspace_user.delete("/workspace_user/{id}}", tags=["Workspace-User"])
async def delete_workspace_user(id: str) -> Any:
    workspace_user = await crud.workspace_user.remove(id=id)
    if not workspace_user:
        raise HTTPException(
            status_code=404, 
            detail="Workspace user is not found.")
    return {"message" : "Successfully deleted."}