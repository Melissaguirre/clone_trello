from app.models.workspace_users import WorkspaceUsers
from app.schemas.workspace_users import WorkspaceUserCreate, WorkspaceUserUpdate
from app.crud.base import CRUDBase


class CRUDWorkspaceUser(CRUDBase[WorkspaceUsers, WorkspaceUserCreate, WorkspaceUserUpdate]):
    ...


workspace_user = CRUDWorkspaceUser(WorkspaceUsers)
