from typing import Any, Dict, Optional, Union, List
from app.models.workspaces import Workspaces
from app.schemas.workspace import *
from app.crud.base import CRUDBase


class CRUDWorkspace(CRUDBase[Workspaces, WorkspaceCreate, WorkspaceUpdate]):
    
    async def filter_name_workspace(self, *, workspace_name: str) -> Workspace:
        return await Workspace.filter(workspace_name=workspace_name).first()


workpaces = CRUDWorkspace(Workspaces)