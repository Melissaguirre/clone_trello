from tortoise.models import Model 
from tortoise import fields


class WorkspaceUsers(Model):
    id = fields.CharField(pk=True, index=True, max_length=50)
    workspace = fields.ForeignKeyField("models.Workspaces", related_name = "Workspace", null=True)
    user = fields.ForeignKeyField("models.Users", related_name = "users1", null=True)
    date = fields.DatetimeField(auto_now=True)
