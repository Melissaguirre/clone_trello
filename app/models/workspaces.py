from tortoise.models import Model 
from tortoise import fields 

class Workspaces(Model):
    id = fields.CharField(pk=True, index=True, max_length=100)
    workspace_name = fields.CharField(max_length=100)
    background_imgURL = fields.TextField(max_length=255)
    starred = fields.BooleanField()
    board_type = fields.TextField(max_length=255)
