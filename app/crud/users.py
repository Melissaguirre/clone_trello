from typing import Any, Dict, Optional, Union, List
from app.models.users import Users
from app.schemas.users import UserCreate, UserUpdate
from app.crud.base import CRUDBase


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):

    async def get(self, *, userID : str)-> Optional[Users]:
        return await Users.get(userID = userID)

    async def get_all(self, *, skip : int = 0, limit : int = 100) -> Users:
        return await Users.all().offset(skip).limit(limit)

    async def create(self, *, obj_in : UserCreate) -> Users:
        db_obj = await Users.create(userID = obj_in.userID, first_name = obj_in.first_name, last_name = obj_in.last_name, address = obj_in.address, city = obj_in.city, state = obj_in.state, Zip = obj_in.Zip, phone = obj_in.phone, email = obj_in.email, avatar_imgURL = obj_in.avatar_imgURL, password = obj_in.password)
        return db_obj

    async def update(self, *, userID : str, db_obj: Users, obj_in : UserCreate) -> Users:
        db_obj = await Users.filter(userID = userID).update(**obj_in.dict(exclude_unset = True))
        return db_obj

    async def remove(self, *, userID : str) -> Users:
        obj = await Users.filter(userID = userID).delete()
        return obj

users = CRUDUser(Users)