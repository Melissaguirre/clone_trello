from typing import Any, Dict, Optional, Union, List
from app.models.cards import Cards
from app.schemas.cards import CardCreate, CardUpdate
from app.crud.base import CRUDBase


class CRUDCard(CRUDBase[Cards, CardCreate, CardUpdate]):

    async def get_all(self, *, skip : int = 0, limit : int = 100) -> List[Cards]:
        return await Cards.all().offset(skip).limit(limit)

    async def get(self, *, cardID : str)-> Optional[Cards]:
        return await Cards.get(cardID = cardID)

    async def create(self, *, obj_in: CardCreate) -> Cards:
        obj_obj = await Cards.create(cardID = obj_in.cardID, card_description = obj_in.card_description, due_date = obj_in.due_date, listID = obj_in.listID)
        return obj_in


    async def update(self, *, cardID : str, db_obj : Cards, obj_in: CardUpdate) -> Cards:
        db_obj = await Cards.filter(cardID = cardID)
        obj_update = await db_obj.update(**obj_in.dict(exclude_unset = True))
        return obj_update

    async def remove(self, *, cardID : str) -> Cards:
        obj =  await Cards.filter(cardID = cardID).delete()
        return obj

cards = CRUDCard(Cards)