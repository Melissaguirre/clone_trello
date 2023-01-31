from tortoise.models import Model 
from tortoise import fields 
from app.models.workspaces import Workspaces

class Lists(Model):
    listID = fields.CharField(pk=True, max_length=225)
    list_name = fields.TextField(max_length=255)
    order = fields.IntField(max_length=100)
    workspace  = fields.ForeignKeyField("models.Workspaces", related_name="workspaces", null=True)