import firebase_admin
import pyrebase
import json
from firebase_admin import auth, credentials, initialize_app, db

from fastapi.responses import JSONResponse
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException, Request, APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from app import schemas, crud

from helpers import firebase_config


cred = credentials.Certificate('helpers/firebase_sdk.json')
firebase_admin.initialize_app(cred, {'databaseURL':'https://project-trello-263a9-default-rtdb.firebaseio.com/'})


ref = db.reference('/users')
# ref.set({
#     'users':
#         {
#             'user1':
#                 {
#                 "id":"1001", 
#                 "first_name":"Mariana", 
#                 "last_name":"Osorio", 
#                 "address":"", "city":"", 
#                 "state":"", "Zip":"", 
#                 "phone":"", 
#                 "email":"mariana@gmail.com", "avatar_imgURL":"", 
#                 "hashed_password":"1212"
#             },
#         }
# })


router = APIRouter()


#get users
@router.get("/api")
async def get_users():
    return ref.get() 


# # create user
# @router.post("")
# async def create_user(user_in: schemas.UserCreate):
#     json_user = jsonable_encoder(user_in)
#     create_user = ref.set(json_user)
#     user = auth.create_user(email=user_in.email, password=user_in.password) 
#     if create_user is None:
#         return {"message": "is None"} 
#     return create_user
        

@router.post("/user")
async def login(user_in: schemas.Login):
    try:
        user = firebase_config.firebase.auth().sign_in_with_email_and_password(email=user_in.email, password=user_in.password)
        jwt = user['idToken']
        return JSONResponse(content={'token': jwt}, status_code=200)
    except:
        return HTTPException(detail={'message': 'There was an error logging in'}, status_code=400) 
    
@router.post("/token/{token}")
async def validate_token(token: str):
    decode_token = auth.verify_id_token(token)
    uid = decode_token['uid']
    return {'uid': uid}