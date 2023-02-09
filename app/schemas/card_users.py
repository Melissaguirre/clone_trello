from pydantic import BaseModel 


class CardUserBase(BaseModel):
    id : str 
    card_id : str
    user_id : str  
    

class CardUserCreate(CardUserBase):
    order : int 
    

class CardUserUpdate(BaseModel):
    order : int


class ReadCardUser(CardUserBase):
    order : int 


class CardUserInDBBase(CardUserBase):
    id : str 
    order : int

    class Config:
        orm_mode = True


class CardUser(CardUserInDBBase):
    ...