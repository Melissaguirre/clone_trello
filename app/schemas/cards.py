from pydantic import BaseModel 
from typing import Optional
from datetime import date
from uuid import UUID

class CardBase(BaseModel):
    id : Optional[UUID]
    card_description : Optional[str] 
    due_date : date
    list_id : Optional[str]


class CardCreate(CardBase):
    ...


class CardUpdate(BaseModel):
    card_description : Optional[str] 
    due_date : date


class ReadCards(CardBase):
    ...


class CardInDBBase(CardBase):
    id : Optional[UUID]

    class Config:
        orm_mode = True


class Card(CardInDBBase):
    ...