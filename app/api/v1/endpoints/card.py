from fastapi import APIRouter, HTTPException 
from typing import List, Any
from app import models, schemas, crud 

card = APIRouter()

#read all cards
@card.get("/card", responde_model = List[schemas.ReadCards], tags = ["Card"])
async def get_cards(skip : int = 0, limit : int = 100) -> Any:
    return await crud.cards.get_all(skip = skip, limit = limit)

#read card by cardID
@card.get("/card/{cardID}", response_model = schemas.Card, tags = ["Card"])
async def get_card(cardID : str) -> Any:
    card = await crud.cards.get(cardID = cardID)
    if not card:
        raise HTTPException(status_code = 404, detail = "Card is not found")
    return card


#create card
@card.post("/card/create", response_model = schemas.Card, tags = ["Card"])
async def create_card(card_in : schemas.CardCreate) -> Any:
    card = await crud.cards.create(card_in)
    return card 

#update card
@card.put("/card/{cardID}", response_model = models.Cards, tags = ["Card"])
async def update_card(user : schemas.Card, card_in : schemas.CardUpdate, cardID : str) -> Any:
    card = await crud.cards.update(card_in, cardID = cardID)
    if not card:
        raise HTTPException(status_code = 404, detail = "Card is not found")
    return card

#delete card 
@card.delete("/card/{cardID}", response_model = schemas.Card, tags = ["Card"])
async def delete_card(cardID : str)-> Any:
    card = await crud.cards.remove(cardID = cardID)
    if not card:
        raise HTTPException(status_code = 404, detail = "Card is not found")
    return card

