from urllib import response

from dotenv import load_dotenv
import os
from fastapi import FastAPI
from google import genai 


load_dotenv()
app=FastAPI()
client=genai.client(api_key=os.getenv("api_key"))

@app.post("/generate")
def generate(prompt:str):
    response=client.models.generate_content(
        model="gemini-3.5-flash-lite",
        content=prompt
    )
    return ("responce":response,text)
#develop a small application
#using react,fastapi,middleware,database