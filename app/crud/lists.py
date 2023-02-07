from typing import Any, Dict, List, Optional, Union
from app.models.lists import Lists
from app.schemas.lists import ListCreate, ListUpdate
from app.crud.base import CRUDBase


class CRUDList(CRUDBase[Lists, ListCreate, ListUpdate]):

    async def get_by_id(self, *, list_id: str) -> Optional[Lists]:
        return await Lists.get(list_id=list_id)

    async def create(self, *, obj_in: ListCreate) -> Lists:
        db_obj = await Lists.create(list_id=obj_in.list_id,
        list_name = obj_in.list_name, order=obj_in.order,
        workspace_id=obj_in.workspace_id)
        return db_obj 

    async def update(self, *, list_id: str, obj_in: ListUpdate) -> Lists:
        data_update = (obj_in.dict(exclude_unset=True))
        db_obj = await Lists.filter(list_id=list_id).update(**data_update)
        if db_obj:
           obj = await self.get(list_id=list_id)
           return obj
        return None 

    async def remove(self, *, list_id: str)-> Lists:
        obj = await Lists.filter(list_id=list_id).delete()
        return obj 

lists = CRUDList(Lists)