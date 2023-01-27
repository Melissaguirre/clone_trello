from pydantic import BaseModel 

class BaseUser(BaseModel):
    userID : str
    first_name : str 
    last_name : str 
    address : str 
    city  : str 
    state  : str 
    Zip : int 
    phone  : str 
    email : str 
    avatar_imgURL : str 

class UserCreate(BaseUser):
    password : str 


class UserUpdate(BaseModel):
    address : str 
    city  : str 
    state  : str 
    Zip : int 
    phone  : str 
    email : str 
    avatar_imgURL : str 

class ReadUser(BaseUser):
    userID : str

class UserInDBBase(BaseUser):
    userID : str

    class Config:
        orm_mode = True

class User(UserInDBBase):
    ...