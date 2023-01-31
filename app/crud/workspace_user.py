from typing import Any, Dict, Optional, Union, List
from app.models.workspace_users import  WorkspaceUsers
from app.schemas.workspace_users import WorkspaceUserCreate, WorkspaceUserUpdate
from app.crud.base import CRUDBase

class CRUDWorkspaceUser(CRUDBase[WorkspaceUsers, WorkspaceUserCreate, WorkspaceUserUpdate]):

    async def get_all(self, *, skip: int = 0, limit: int = 100) -> List[WorkspaceUsers]:
        return await WorkspaceUsers.all().offset(skip).limit(limit)


    async def get(self, *, workspaceID: str) -> Optional[WorkspaceUsers]:
        return await WorkspaceUsers.get(workspaceID=workspaceID)

    async def create(self, *, obj_in: WorkspaceUserCreate) -> WorkspaceUsers:
        db_obj = await WorkspaceUsers.create(
            workspaceID=obj_in.workspaceID,
            userID=obj_in.userID, 
            date=obj_in.date)
        return db_obj

    async def update(self, *, db_obj: WorkspaceUsers, obj_in: WorkspaceUserUpdate, workspaceID: str) -> WorkspaceUsers:
        db_obj = await WorkspaceUsers.filter(workspaceID=workspaceID)
        obj_update=db_obj.update(**obj_in.dict(exclude_unset=True))
        return obj_update

    async def remove(self, * workspaceID: str) -> WorkspaceUsers:
        obj = await WorkspaceUsers.filter(workspaceID=workspaceID).delete()
        return obj 

workspace_user = CRUDWorkspaceUser(WorkspaceUsers)