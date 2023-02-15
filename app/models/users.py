from tortoise.models import Model
from tortoise import fields


class Users(Model):
    id = fields.UUIDField(pk=True)
    first_name = fields.CharField(max_length=100)
    last_name = fields.CharField(max_length=100)
    address = fields.CharField(max_length=100)
    city = fields.CharField(max_length=100)
    state = fields.CharField(max_length=100)
    Zip = fields.IntField(max_length=100)
    phone = fields.CharField(max_length=50)
    email = fields.CharField(max_length=100)
    avatar_imgURL = fields.CharField(max_length=225)
    hashed_password = fields.CharField(max_length=100)
    
