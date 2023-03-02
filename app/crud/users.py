import uuid

from typing import Optional, List

from app.models.users import Users
from app.schemas.users import UserCreate, UserUpdate, UserInDB
from app.crud.base import CRUDBase

from app.core.security import get_password_hash, verify_password, generate_token


class CRUDUser(CRUDBase[Users, UserCreate, UserUpdate]):
    
  
    async def filter_name_user(self, *, first_name: str) -> Users:
        return await Users.filter(first_name=first_name).first()
        
    async def create(self, *, obj_in: UserCreate) -> dict:
        
        db_obj = await Users.create(id=obj_in.id,
        first_name = obj_in.first_name, last_name=obj_in.last_name,
        address=obj_in.address, city=obj_in.city,state=obj_in.state, Zip=obj_in.Zip,phone=obj_in.phone, email=obj_in.email, avatar_imgURL=obj_in.avatar_imgURL,hashed_password=get_password_hash(obj_in.password), is_active=obj_in.is_active, token=obj_in.token)
        
        return {"message": "check your email"}
     
    async def verify_token(*, token: str) -> str:
        result = await Users.filter(token=token).first()
        if result:
            user = Users.is_active = True
            return {"message": "User is active"}
        else:
            return None
        
   
users = CRUDUser(Users)