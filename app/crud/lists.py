from typing import Any, Dict, List, Optional, Union
from app.models.lists import Lists
from app.schemas.lists import ListCreate, ListUpdate
from app.crud.base import CRUDBase


class CRUDList(CRUDBase[Lists, ListCreate, ListUpdate]):

    async def get_all(self, *, skip : int = 0 , limit : int = 100) -> List[Lists]:
        return Lists.all().offset(skip).limit(limit)

    async def get(self, *, listID : str) -> Optional[Lists]:
        return await Lists.get(listID = listID)

    async def create(self, *, obj_in : ListCreate) -> Lists:
        db_obj = await Lists.create(listID = obj_in.listID,
        lists_name = obj_in.list_name, order =  obj_in.order,
        workspaceID = obj_in.workspaceID)
        return db_obj 

    async def update(self, *, listID :str, obj_in : ListUpdate) -> Lists:
        db_obj = await Lists.filter(listID = listID)
        obj_update = db_obj.update(**obj_in.dict(exclude_unset = True))
        return obj_update

    async def remove(self, *, listID : str)-> Lists:
        obj = await Lists.filter(listID = listID).delete()
        return obj 

lists = CRUDList(Lists)