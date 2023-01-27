from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union 
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
   
   def __init__(self, model : Type[ModelType]):
    self.model = model 

    async def get_all(self, *, skip : int = 0, limit : int = 100) -> List[ModelType]:
        return await self.model.all().offset(skip).limit(limit)

    async def get(self, id : str) -> ModelType:
        return await self.model.get(self.model.id == id) 

    async def create(self, *, obj_in = CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = await self.model.create(**obj_in_data)
        return db_obj

    async def update(
        self, *, id: Any, db_obj : ModelType, obj_in: UpdateSchemaType ) -> ModelType:
        db_obj = await self.model.filter(id = id)  
        data_update = jsonable_encoder(obj_in)
        obj_update = await db_obj.update(**data_update.dict(exclude_unset = True))
        return obj_update

    async def remove(self, *, id : str) -> ModelType:
        obj = await self.model.filter(id = id).delete()
        return obj

