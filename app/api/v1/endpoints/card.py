from fastapi import APIRouter, HTTPException
from fastapi.encoders import jsonable_encoder
from typing import List, Any, Optional
from app import models, schemas, crud
import tortoise


router = APIRouter()


# read all cards
@router.get("", response_model=List[schemas.ReadCards])
async def get_cards(skip: int = 0, limit: int = 100) -> Any:
    return await crud.cards.get_all(skip=skip, limit=limit)


#count cards
@router.get("/count")
async def count_cards(self, *, skip: int = 0, limit: int = 100):
    cards = await crud.cards.get_all(skip=skip, limit=limit)
    return {"registered users": cards}
    
    
# read card by cardID
@router.get("/{id}", response_model=schemas.Card)
async def get_card(*, id: str) -> Any:
    try: 
        return await crud.cards.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Card is not found")


# create card
@router.post("", response_model=schemas.Card)
async def create_card(*, card_in: schemas.CardCreate) -> Any:
    try:
        return await crud.cards.create(obj_in=card_in)
    except tortoise.exceptions.IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="The card already exists in the system.")


# update card
@router.put("/{id}")
async def update_card(*, id: str, card_in: schemas.CardUpdate, ) -> Any:
    card = await crud.cards.update(id=id, obj_in=card_in)
    if not card:
        raise HTTPException(
            status_code=404,
            detail="Card is not found")
    return card


# delete card
@router.delete("/{id}")
async def delete_card(id: str) -> Any:
    card = await crud.cards.remove(id=id)
    if not card:
        raise HTTPException(
            status_code=404,
            detail="Card is not found")
    return {"message": "Successfully deleted"}
