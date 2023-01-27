from pydantic import BaseModel 

class CardBase(BaseModel):
    card_description : str 
    due_date : int 
    listID : str 

class CardCreate(CardBase):
    cardID : str 

class CardUpdate(BaseModel):
    card_description : str 
    due_date : int 


class ReadCards(CardBase):
   cardID : str

class CardInDBBase(CardBase):
    cardID : str 

    class Config:
        orm_mode = True

class Card(CardInDBBase):
    ...