from tortoise.models import Model 
from tortoise import fields 
from app.models.lists import Lists

class Cards(Model):
    id = fields.CharField(pk=True, index=True, max_length=50)
    card_description = fields.TextField(max_length=225)
    due_date = fields.IntField()
    list = fields.ForeignKeyField("models.Lists", related_name="lists", null=False)
