import firebase_admin
from firebase_admin import auth, credentials, initialize_app, db

cred = credentials.Certificate('helpers/firebase_sdk.json')
firebase_admin.initialize_app(cred, {'databaseURL':'https://project-trello-263a9-default-rtdb.firebaseio.com/'})

