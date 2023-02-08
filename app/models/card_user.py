from tortoise import fields
from tortoise.models import Model


class CardUsers(Model):
    id : fields.CharField(pk=True, index=True, max_length=50)
    card = fields.ForeignKeyField("models.Cards", related_name="cards", null=True)
    user = fields.ForeignKeyField("models.Users", related_name="users", null=True)
    order = fields.IntField()
