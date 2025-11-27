import os
from fastapi import HTTPException
from dotenv import load_dotenv
import httpx
import asyncio

load_dotenv()



HF_API_KEY=os.getenv("HF_API_KEY")

API_URL_TO_FR = "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-en-fr"
API_URL_TO_EN = "https://router.huggingface.co/hf-inference/models/Helsinki-NLP/opus-mt-fr-en"

headers = {"Authorization": f"Bearer {HF_API_KEY}"}

async def translate_text(text:str,language:str):
    try:
            API_URL=API_URL_TO_FR if language=='en-to-fr' else API_URL_TO_EN      
            async with httpx.AsyncClient() as client:
             response = await client.post(
              API_URL  ,
              headers=headers,
              json={"inputs":text},
              timeout=30.0
            )
            response.raise_for_status()
            
            return response.json()
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
