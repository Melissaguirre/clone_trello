from fastapi import APIRouter, HTTPException 
from fastapi.encoders import jsonable_encoder
from typing import List, Any
from app import models, schemas, crud 

card = APIRouter()

#read all cards
@card.get("/card", response_model=List[schemas.ReadCards], tags=["Card"])
async def get_cards(skip: int = 0, limit: int = 100) -> Any:
    return await crud.cards.get_all(skip=skip, limit=limit)

#read card by cardID
@card.get("/card/{cardID}", response_model=schemas.Card, tags=["Card"])
async def get_card(cardID: str) -> Any:
    card = await crud.cards.get(cardID=cardID)
    if not card:
        raise HTTPException(
            status_code=404, 
            detail="Card is not found")
    return card


#create card
@card.post("/card", response_model=schemas.Card, tags=["Card"])
async def create_card(*, card_in: schemas.CardCreate) -> Any:
    card = await crud.cards.create(obj_in=card_in)
    return card 

#update card
@card.put("/card/{cardID}", response_model=schemas.Card, tags=["Card"])
async def update_card(*, cardID : str, card_in: schemas.CardUpdate, ) -> Any:
    card  = await crud.cards.update(cardID=cardID, obj_in=card_in)
    if not card:
        raise HTTPException(
            status_code=404, 
            detail="Card is not found")
    return card

#delete card 
@card.delete("/card/{cardID}", tags=["Card"])
async def delete_card(cardID : str) -> Any:
    card = await crud.cards.remove(cardID=cardID)
    if not card:
        raise HTTPException(
            status_code = 404, 
            detail = "Card is not found")
    return {"message" : "Successfully deleted"}

