from tortoise.models import Model 
from tortoise import fields 

class Lists(Model):
    list_id = fields.UUIDField(pk=True)
    list_name = fields.TextField(max_length=255)
    order = fields.IntField(max_length=100)
    workspace  = fields.ForeignKeyField("models.Workspaces", related_name="workspaces", null=False)