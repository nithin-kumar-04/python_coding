from dotenv import load_dotenv
import os
from fastapi import FastAPI, HTTPException
from google import genai
from pydantic import BaseModel

load_dotenv()
app = FastAPI()
client = genai.Client(api_key=os.getenv("api_key"))

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate(request: PromptRequest):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=request.prompt,
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"response": response.text}

#develop a small application
#using react,fastapi,middleware,database