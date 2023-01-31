from typing import Any, Dict, Optional, Union, List
from app.models.card_user import CardUsers
from app.schemas.card_users import CardUserCreate, CardUserUpdate
from app.crud.base import CRUDBase

class CRUDCardUser(CRUDBase[CardUsers, CardUserCreate, CardUserUpdate]):

    async def get_all(self, *, skip: int = 0, limit: int = 100) -> List[CardUsers]:
        return await CardUsers.all().offset(skip).limit(limit)

    #read by cardID
    async def get(self, * , cardID: str) -> Optional[CardUsers]:
        return await CardUsers.get(cardID=cardID)


    #create carduser
    async def create(self, *, obj_in: CardUserCreate) -> CardUsers:
        db_obj = await CardUsers.create(cardID=obj_in.cardID, userID=obj_in.userID, order=obj_in.order)
        return db_obj

    #update carduser
    async def update(self, *, cardID: str, db_obj: CardUsers, obj_in: CardUserUpdate) -> CardUsers:
        db_obj = await CardUsers.filter(cardID=cardID)
        obj_update = await db_obj.update(**obj_in.dict(exclude_unset=True))
        return obj_update

    #delete carduser
    async def remove(self, *, cardID: str)-> CardUsers:
        obj = await CardUsers.filter(cardID=cardID).delete()
        return obj

card_users = CRUDCardUser(CardUsers)
