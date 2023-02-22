from typing import Optional, List

from app.models.users import Users
from app.schemas.users import UserCreate, UserUpdate, UserInDB
from app.crud.base import CRUDBase


from app.core.security import get_password_hash, verify_password


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    
    # async def get_by_id(self, *, id: str) -> Optional[Users]:
    #     return await Users.get(id=id)
  
    async def filter_name_user(self, *, first_name: str) -> Users:
        return await Users.filter(first_name=first_name).first()
        
    async def create(self, *, obj_in: UserCreate) -> Users:
        db_obj = await Users.create(id=obj_in.id,
        first_name = obj_in.first_name, last_name=obj_in.last_name,
        address=obj_in.address, city=obj_in.city,state=obj_in.state, Zip=obj_in.Zip,phone=obj_in.phone, email=obj_in.email, avatar_imgURL=obj_in.avatar_imgURL,hashed_password=get_password_hash(obj_in.password))
        return db_obj 
        
        
    async def authenticate(self, *, email: str, password: str) -> Optional[Users]:
        user = await self.model.get(email=email)
        if not user:
            return None 
        if not verify_password(password, user.hashed_password):
            return None
        return user 
   
users = CRUDUser(Users)