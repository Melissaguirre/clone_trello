from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

class BaseUser(BaseModel):
    id : Optional[str] 
    first_name : Optional[str]
    last_name : Optional[str] 
    address : Optional[str]
    city : Optional[str] 
    state : Optional[str]
    Zip : Optional[int]
    phone  : Optional[str] 
    email : Optional[str] 
    avatar_imgURL : Optional[str] 

    class Config:
        orm_mode = True


class UserCreate(BaseUser):
    id : Optional[str]
    password : str = Field(..., min_length=6)


class UserUpdate(BaseModel):
    address : Optional[str] 
    city  : Optional[str]
    state  : Optional[str] 
    Zip : Optional[int] 
    phone  : Optional[str] 
    email : Optional[str]
    avatar_imgURL : Optional[str]


class ReadUser(BaseUser):
    ...


class UserInDBBase(BaseUser):
    id : Optional[str]
    
    class Config:
        orm_mode = True

class User(UserInDBBase):
    ...


class UserInDB(UserInDBBase):
    hashed_password: str
    
class Login(BaseModel):
    email : str 
    password : str 
    