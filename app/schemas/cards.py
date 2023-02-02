from pydantic import BaseModel 
from typing import Optional

class CardBase(BaseModel):
    id : str 
    card_description : Optional[str] 
    due_date : Optional[int] 
    list_id : Optional[str]

class CardCreate(CardBase):
    ...

class CardUpdate(BaseModel):
    card_description : Optional[str] 
    due_date : int


class ReadCards(CardBase):
    ...

class CardInDBBase(CardBase):
    id : str 

    class Config:
        orm_mode = True

class Card(CardInDBBase):
    ...