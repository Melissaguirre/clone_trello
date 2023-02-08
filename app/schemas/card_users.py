from pydantic import BaseModel 
from typing import Optional

class CardUserBase(BaseModel):
    card_id : str
    user_id : str
    order : int 
    

class CardUserCreate(CardUserBase):
    id: Optional[str]
  


class CardUserUpdate(BaseModel):
    order : int


class ReadCardUser(CardUserBase):
    ...


class CardUserInDBBase(CardUserBase):
    id : str 

    class Config:
        orm_mode = True

class CardUser(CardUserInDBBase):
    ...