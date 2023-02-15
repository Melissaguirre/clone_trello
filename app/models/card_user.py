from tortoise.models import Model 
from tortoise import fields


class CardUsers(Model):
    id : fields.UUIDField(pk=True)
    card = fields.ForeignKeyField("models.Cards", related_name="cards", null=True)
    user = fields.ForeignKeyField("models.Users", related_name="users", null=True)
    order = fields.IntField()
