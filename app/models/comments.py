from tortoise.models import Model 
from tortoise import fields 

class Comments(Model):
    id = fields.UUIDField(pk=True)
    activity = fields.BooleanField()
    comment_content = fields.TextField(max_length=225)
    date_created = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)
    card = fields.ForeignKeyField("models.Users", relate_name="users", null=True)
    user = fields.ForeignKeyField("models.Cards", relate_name="cards", null=True)