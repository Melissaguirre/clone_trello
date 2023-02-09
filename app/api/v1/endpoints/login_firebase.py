# from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
# from fastapi import Depends, HTTPException, status, Response, APIRouter, Depends
# from firebase_admin import auth, credentials, initialize_app

# credential = credentials.Certificate('service_account_keys.json')
# initialize_app(credential)

# def get_user_token(res: Response, credential: HTTPAuthorizationCredentials=Depends(HTTPBearer(auto_error=False))):
#     if credential is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Bearer authentication is needed",
#             headers={'WWW-Authenticate': 'Bearer realm="auth_required"'},
#         )
#     try:
#         decoded_token = auth.verify_id_token(credential.credentials)
#     except Exception as err:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail=f"Invalid authentication from Firebase. {err}",
#             headers={'WWW-Authenticate': 'Bearer error="invalid_token"'},
#         )
#     res.headers['WWW-Authenticate'] = 'Bearer realm="auth_required"'
#     return decoded_token

# route = APIRouter()

# @route.get("/api/")
# async def hello():
#     return {"msg":"Hello, this is API server"} 


# @route.get("/api/user_token")
# async def hello_user(user = Depends(get_user_token)):
#     return {"msg":"Hello, user","uid":user['uid']} 