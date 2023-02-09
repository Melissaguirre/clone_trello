from typing import Any, Dict, Optional, Union, List
from app.models.workspaces import Workspaces
from app.schemas.workspace import *
from app.crud.base import CRUDBase


class CRUDWorkspace(CRUDBase[Workspaces, WorkspaceCreate, WorkspaceUpdate]):
    ...


workpaces = CRUDWorkspace(Workspaces)