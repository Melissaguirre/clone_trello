import pyrebase 

fireBaseConfig = {
    "apiKey": "AIzaSyBpT4-aDIICsRJngG2j__8epCpmIRPsJfI",
    "authDomain": "project-trello-263a9.firebaseapp.com",
    "databaseURL": "https://project-trello-263a9-default-rtdb.firebaseio.com",
    "projectId": "project-trello-263a9",
    "storageBucket": "project-trello-263a9.appspot.com",
    "messagingSenderId": "384564733813",
    "appId": "1:384564733813:web:d300a21da6edebc1b8d53c",
    "measurementId": "G-XRZ6K8FTM5"
  }

firebase = pyrebase.initialize_app(fireBaseConfig)