from tortoise.models import Model 
from tortoise import fields 

class Cards(Model):
    id = fields.UUIDField(pk=True)
    card_description = fields.TextField(max_length=225)
    due_date = fields.DateField()
    list = fields.ForeignKeyField("models.Lists", related_name="lists", null=False)
