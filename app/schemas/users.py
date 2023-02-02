from pydantic import BaseModel
from typing import Optional

class BaseUser(BaseModel):
    id : str
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
    id : str
    password : str 


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
    id : str

    class Config:
        orm_mode = True

class User(UserInDBBase):
    ...
