from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List, Any, Optional
from app import models, schemas, crud

card = APIRouter()


# read all cards
@card.get("/card", response_model=List[schemas.ReadCards], tags=["Card"])
async def get_cards(skip: int = 0, limit: int = 100) -> Any:
    return await crud.cards.get_all(skip=skip, limit=limit)


# read card by cardID
@card.get("/card/{id}", response_model=schemas.Card, tags=["Card"])
async def get_card(*, id: str) -> Any:
    card = await crud.cards.get(id=id)
    if not card:
        raise HTTPException(
            status_code=404,
            detail="Card is not found")
    return card


# create card
@card.post("/card", response_model=schemas.Card, tags=["Card"])
async def create_card(*, card_in: schemas.CardCreate) -> Any:
    card = await crud.cards.create(obj_in=card_in)
    if not card:
        raise HTTPException(
            status_code=400,
            detail="The card already exists in the system.")
    return card


# update card
@card.put("/card/{id}", tags=["Card"])
async def update_card(*, id: str, card_in: schemas.CardUpdate, ) -> Any:
    card = await crud.cards.update(id=id, obj_in=card_in)
    if not card:
        raise HTTPException(
            status_code=404,
            detail="Card is not found")
    return card

# delete card


@card.delete("/card/{id}", tags=["Card"])
async def delete_card(id: str) -> Any:
    card = await crud.cards.remove(id=id)
    if not card:
        raise HTTPException(
            status_code=404,
            detail="Card is not found")
    return {"message": "Successfully deleted"}
