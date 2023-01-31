from pydantic import BaseModel
from typing import Optional

class BaseUser(BaseModel):
    userID : str
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
    userID : str
    password : str 


class UserUpdate(BaseModel):
    userID : str
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
    userID : str

    class Config:
        orm_mode = True

class User(UserInDBBase):
    ...

class UserOut(BaseModel):
    userID : str 
    address : Optional[str] 
    city  : Optional[str] 
    state  : Optional[str]
    Zip : Optional[int]
    phone  : Optional[str] 
    email : Optional[str] 
    avatar_imgURL : Optional[str]

    class Config:
        orm_mode = True
