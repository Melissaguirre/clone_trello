from tortoise.models import Model 
from tortoise import fields
from app.models.cards import Cards
from app.models.users import Users

class CardUsers(Model):
    card = fields.ForeignKeyField("models.Cards", related_name="cards", null=True)
    user = fields.ForeignKeyField("models.Users", related_name="users", null=True)
    order = fields.IntField()
