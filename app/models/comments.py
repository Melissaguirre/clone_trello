from tortoise.models import Model 
from tortoise import fields 
from app.models.users import Users
from app.models.cards import Cards

class Comments(Model):
    id = fields.CharField(pk=True, index = True, max_length=255)
    activity = fields.BooleanField()
    comment_content = fields.TextField(max_length=225)
    date_created = fields.DatetimeField(auto_now_add=True)
    date_modified = fields.DatetimeField(auto_now=True)
    card = fields.ForeignKeyField("models.Users", relate_name="users", null=True)
    user = fields.ForeignKeyField("models.Cards", relate_name="cards", null=True)