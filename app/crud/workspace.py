from typing import Any, Dict, Optional, Union, List
from app.models.workspaces import Workspaces
from app.schemas.workspace import *
from app.crud.base import CRUDBase

class CRUDWorkspace(CRUDBase[Workspaces, WorkspaceCreate, WorkspaceUpdate]):

    async def get_all(self, *, skip: int = 100, limit: int = 100) -> List[Workspaces]:
        return await Workspaces.all().offset(skip).limit(limit)

    async def get(self, *, workspaceID: str) -> Optional[Workspaces]:
        return await Workspaces.get(workspaceID=workspaceID)

    async def create(self, *, obj_in: WorkspaceCreate) -> Workspaces:
        db_obj = await Workspaces.create(
            workspaceID=obj_in.workspaceID,
            workspace_name=obj_in.workspace_name, 
            background_imgURL=obj_in.background_imgURL, 
            starred=obj_in.starred, 
            board_type=obj_in.board_type )
        return db_obj

    async def update(self, *, workspaceID: str, db_obj: Workspaces, obj_in: WorkspaceUpdate) -> Workspaces:
        db_obj = await Workspaces.filter(workspaceID=workspaceID)
        obj_update=await db_obj.update(**obj_in.dict(excude_unset=True))
        return await obj_update

    async def remove(self, *, workspaceID: str) -> Workspaces:
        obj = await Workspaces.filter(workspaceID=workspaceID).delete()
        return obj

workpaces = CRUDWorkspace(Workspaces)