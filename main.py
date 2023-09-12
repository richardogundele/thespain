from typing import Optional
from fastapi import FastAPI
app = FastAPI()
from pymongo import MongoClient

import openai, os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from apirequests import text_to_text_response, convert_text_to_speech, chat_history

openai.api_key = os.getenv("OPENAI_API_KEY")

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
@app.get("/")
def read_root():
    return {"ThespAIn": "/text /speech /itworking"}
           
#get history
@app.post("/history")
async def history():
    history = chat_history()
    return history

#get text
@app.post("/text")
async def post_text(textinput):
    message = text_to_text_response(textinput)
    return message

#get speech
@app.post("/speech")
# async def post_speech(file:UploadFile= File(...)):
    # audio_input = open("speech.mp3", "rb")
    #get and save file from frontend
    # with open(file.filename, "wb") as buffer:
    #     buffer.write(file.file.read())
    # audio_input = open(file.filename, "rb")
    # text_decoded = convert_speech_to_text(audio_input)  
    # print(text_decoded)
    # if not text_decoded:
    #     raise HTTPException(status_code=400, detail="Failed to decode Audio")
async def post_speech(speech_converted):
    chat_response = text_to_text_response(speech_converted)
    print(chat_response)
    if not chat_response:
        return HTTPException(status_code=400, details="Failure to get chat response")
    
    audio_output = convert_text_to_speech(chat_response)
    if not audio_output:
        return HTTPException(status_code=400, detail="failed to get audio")
    
    def iterfile():
        yield audio_output
        
    return StreamingResponse(iterfile(), media_type="application/octet-stream")


@app.post("/text_to_speech")
async def text_to_speech(covert):
    message = text_to_text_response(text_input=covert)

    audio_output = convert_text_to_speech(message)
    if not audio_output:
        return HTTPException(status_code=400, detail="failed to get audio")
    
    def iterfile():
        yield audio_output
        
    return StreamingResponse(iterfile(), media_type="application/octet-stream")
