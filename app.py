from fastapi import FastAPI
from fastapi import APIRouter, Depends
from service import VocalizeService

app = FastAPI()
router = APIRouter()
app.include_router(router)


def get_service() -> VocalizeService:
    return VocalizeService()


@app.post("/create-transcription")
async def speech_to_text(duration: int, service: VocalizeService = Depends(get_service)):
    return service.create_transcription(duration)

@app.post("/create-speech")
async def text_to_speech(text: str, service: VocalizeService = Depends(get_service)):
    return service.text_to_speech(text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
