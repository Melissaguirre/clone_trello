from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union 
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
   
    def __init__(self, model: Type[ModelType]):
        self.model = model 

    async def get_all(self, *, skip: int = 0, limit: int = 100) -> List[ModelType]:
        return await self.model.all().offset(skip).limit(limit)

    async def get_by_id(self, id: str) -> Optional[ModelType]:
        return await self.model.get(id=id) 
    
    async def create(self, *, obj_in=CreateSchemaType) -> ModelType:
        obj_in_data =(obj_in.dict(exclude_unset=True))
        db_obj = await self.model.create(**obj_in_data)
        return db_obj

    async def update(
        self, *, id: Any, obj_in: UpdateSchemaType) -> ModelType:
        data_update = (obj_in.dict(exclude_unset=True))
        db_obj = await self.model.filter(id=id).update(**data_update)
        if db_obj:
           obj = await self.get_by_id(id=id)
           return obj
        return None 

    async def remove(self, *, id: str) -> ModelType:
        obj = await self.model.filter(id=id).delete()
        return obj

