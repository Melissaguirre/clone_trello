from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Any
from app import crud, models, schemas
import tortoise


router = APIRouter()
#read all workspeaces
@router.get("", response_model=List[schemas.ReadWorkspace])
async def get_workspaces(skip: int = 0, limit: int = 100) -> Any:
    return await crud.workpaces.get_all(skip=skip, limit=limit)

#read workspaces by workspaceID
@router.get("/{id}", response_model=schemas.Workspace)
async def get_workspaces(id: str)-> Any:
    try: 
        return await crud.workpaces.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="Workspace is not found")


#create workspace
@router.post("",response_model=schemas.Workspace)
async def create_workspace(workspace_in: schemas.WorkspaceCreate) -> Any:
    try:
        return await crud.workpaces.create(obj_in=workspace_in)
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The workspace with this id already exists")

#update workspace
@router.put("/{id}",response_model=schemas.Workspace)
async def update_workspace(workspace_in: schemas.WorkspaceUpdate, id: str)-> Any:
    workspace = await crud.workpaces.update(id=id, obj_in=workspace_in)
    if not workspace:
        raise HTTPException(
            status_code=404, 
            detail = "Workspace is not found")
    return workspace 

#delete workspace
@router.delete("/{id}")
async def delete_workspace(id: str) -> Any:
    workspace = await crud.workpaces.remove(id=id)
    if not workspace:
        raise HTTPException(
            status_code = 404, 
            detail = "Workspace is not found")
    return {"message" : "Successfully deleted"}

