from pydantic import BaseModel 
from typing import Optional

class CardBase(BaseModel):
    cardID : str 
    card_description : Optional[str] 
    due_date : Optional[int] 
    listID : str 

class CardCreate(CardBase):
    ...

class CardUpdate(BaseModel):
    card_description : Optional[str] 
    due_date : Optional[int] 


class ReadCards(CardBase):
   cardID : str

class CardInDBBase(CardBase):
    cardID : str 

    class Config:
        orm_mode = True

class Card(CardInDBBase):
    ...