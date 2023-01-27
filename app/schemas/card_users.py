from pydantic import BaseModel 

class CardUserBase(BaseModel):
    cardID : str
    userID : str  
    

class CardUserCreate(CardUserBase):
    order : int 

class CardUserUpdate(BaseModel):
    ...

class ReadCardUser(CardUserBase):
    order : int 

class CardUserInDBBase(CardUserBase):
    cardID : str 

    class Config:
        orm_mode = True

class CardUser(CardUserInDBBase):
    ...