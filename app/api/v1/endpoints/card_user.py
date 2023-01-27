from fastapi import APIRouter, HTTPException 
from typing import List, Any
from app import models, schemas, crud

card_user = APIRouter()

#read all card_user 
@card_user.get("/card_user", response_model = List[schemas.ReadCardUser], tags = ["Card-User"])
async def read_card_users(skip : int = 0, limit : int = 100)-> Any:
    return await crud.card_users.get_all(skip = skip, limit = limit)

#read card_user 
@card_user.get("/card_user", response_model = schemas.CardUser, tags = ["Card-User"])
async def get_card_user(cardID : str)-> Any:
    return await crud.card_users.get(cardID = cardID)

#create card_user
@card_user.post("/card_user/create", response_model = schemas.CardUser, tags = ["Card-User"])
async def create_card_user(card_user_in : schemas.CardUserCreate)-> Any:
    card_user = await crud.card_users.create(card_user_in)
    return card_user 

#update card_user
@card_user.put("/card_user/{cardID}",response_model = schemas.CardUser,  tags = ["Card-User"])
async def update_card_user(cardID : str, card_user : models.CardUsers, card_user_in : schemas.CardUserUpdate)-> Any:
    card_user = await crud.card_users.update(card_user_in, cardID = cardID)
    return card_user

#delete card_user
@card_user.delete("/card_user/{cardID}", response_model = schemas.CardUser, tags = ["Card-User"])
async def delete_card_user(cardID : str)-> Any:
    card_user = await crud.card_users.remove(cardID = cardID)
    return card_user

