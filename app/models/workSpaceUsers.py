from tortoise.models import Model 
from tortoise import fields
from app.models.users import Users
from app.models.workspaces import Workspaces

class WorkspaceUsers(Model):
    workspaceID = fields.ForeignKeyField("models.Workspace", related_name = "workspace", null = True)
    userID = fields.ForeignKeyField("models.Users", related_name = "users", null = True)
    Date = fields.DatetimeField(auto_now = True)
