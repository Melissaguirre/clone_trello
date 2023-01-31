from tortoise.models import Model 
from tortoise import fields
from app.models.users import Users
from app.models.workspaces import Workspaces

class WorkspaceUsers(Model):
    workspace = fields.ForeignKeyField("models.Workspaces", related_name = "Workspace", null=True)
    user = fields.ForeignKeyField("models.Users", related_name = "users1", null=True)
    Date = fields.DatetimeField(auto_now=True)
