from fastapi import APIRouter, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List, Any
from app.models.card_user import CardUsers
from app import models, schemas, crud
import tortoise

card_user = APIRouter()

#read all card_user 
@card_user.get("/card_user", response_model=List[schemas.ReadCardUser], tags=["Card-User"])
async def read_card_users(skip: int = 0, limit: int = 100) -> Any:
    return await crud.card_users.get_all(skip=skip, limit=limit)

#read card_user 
@card_user.get("/card_user/{id}", response_model=schemas.CardUser, tags=["Card-User"])
async def get_card_user(id: str) -> Any:
    try:
        return await crud.card_users.get_by_id(id=id)
    except tortoise.exceptions.DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Card user is not found")

#create card_user
@card_user.post("/card_user", response_model=schemas.CardUser, tags=["Card-User"])
async def create_card_user(*, card_user_in: schemas.CardUserCreate) -> Any:
    try:
        return await crud.card_users.create(obj_in=card_user_in)
    except tortoise.exceptions.Integrity.Error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The card user with this id already exists"
        ) 

#update card_user
@card_user.put("/card_user/{id}",response_model=schemas.CardUser, tags=["Card-User"])
async def update_card_user(*, id: str, card_user_in: schemas.CardUserUpdate) -> Any:
    card_user = await crud.card_users.update(id=id, obj_in=card_user_in)
    if not card_user:
        raise HTTPException(
            status_code=404, 
            detail="Card-User is not found")
    return None 

#delete card_user
@card_user.delete("/card_user/{id}", tags=["Card-User"])
async def delete_card_user(id: str) -> Any:
    card_user = await crud.card_users.remove(id=id)
    if not card_user:
        raise HTTPException(
            status_code=404, 
            detail = "Card user is not found")
    return {"message" : "Successfully deleted"}
