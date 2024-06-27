from fastapi import FastAPI
from pydantic import BaseModel
from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status

from service import VocalizeService

app = FastAPI()
router = APIRouter()
app.include_router(router)


def get_service() -> VocalizeService:
    return VocalizeService()


class Data(BaseModel):
    payload: Any


@app.get("/test")
async def read_items(service: VocalizeService = Depends(get_service)):
    return "a"


@app.post("/create-transcription")
async def create_transcription(duration: int, service: VocalizeService = Depends(get_service)):
    return service.create_transcription(duration)

@app.post("/create-voice")
async def create_voice(text: str, service: VocalizeService = Depends(get_service)):
    return service.speak(text)

@app.post("/create-voice-openai")
async def create_voice(text: str, service: VocalizeService = Depends(get_service)):
    return service.create_voice(text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
# 192.168.1.40:8000
