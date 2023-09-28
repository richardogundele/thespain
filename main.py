from typing import Optional
import openai, os, sqlite3, time, datetime
from mongo import *
from fastapi import HTTPException
from bson import ObjectId  # Import ObjectId from bson module
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from apirequests import text_to_text_response
from database import export_chat_data_to_jsonl
app = FastAPI()

origins = [ 
           "https://localhost:5173",
           "hhtps://localhost:5174",
           "https://localhost:4173",
           "https://localhost:3000",
           ]

app.add_middleware( 
                   CORSMiddleware, 
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
)

# # Initialize the MongoDB client and database
# mongo_client = MongoClient(os.getenv("MONGO_URI"))

# db = mongo_client["chat_app"]

openai.api_key = "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"

@app.get("/")
def read_root():
    return {"ThespAIn": "/Welcome To ThespAIn Backend Code"}

# User registration endpoint
@app.post("/getstarted")
async def get_started(email):
    # Check if the email already exists in the database
    existing_user = db.users.find_one({"user_email": email})
    
    if existing_user:
        # Email already exists, no need to insert it again
        return {"message": "User signed in successfully"}
    else:
        # Email doesn't exist, so insert it as a new user
        db.users.insert_one({"user_email": email})
        return {"message": "User registered successfully"}

@app.post("/text")
async def post_text(email, textinput):
    # Get the response from the OpenAI model
    message = text_to_text_response(textinput)
    
    # Save the conversation to the database
    db.chat_history.insert_one({
        "user_email": email,
        "text_input": textinput,
        "message": message,
        "timestamp": datetime.datetime.now()
    })
    
    print("text message posted successfully")
    return message

# get speech
@app.post("/speech")
async def post_speech(email, file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    
    audio_input = open(file.filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_input)
    
    text_decoded = transcript["text"]
    
    if not text_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode Audio")
    
    message = text_to_text_response(text_decoded)
    return message




# get history
@app.get("/history/{email}")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "user_email": item["user_email"],
            "text_input": item["text_input"],
            "message": item["message"],
        }
        for item in db.chat_history.find({"user_email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")

    # Return chat history as a JSON response
    return {"chat_history": chat_history}



@app.post("/export_for_fine_tuning")
async def trigger_export():
    # Implement your export logic here
    # You can export data to a JSON file or any other desired format
    return {"message": "Export triggered successfully"}
