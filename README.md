# Speech <-> Transcript Service API

This repository contains a FastAPI-based web service for speech transcription and synthesis. The service provides endpoints for converting audio to text (speech-to-text) and text to audio (text-to-speech) using the `VocalizeService`.

## Features

- **Speech-to-Text**: Convert audio input into text transcriptions.
- **Text-to-Speech**: Generate audio output from text input.

## Endpoints

### Create Transcription
- **URL**: `/create-transcription`
- **Method**: POST
- **Parameters**:
  - `duration` (int): The duration of the audio to be transcribed.
- **Response**: Transcription of the provided audio duration.

### Create Speech
- **URL**: `/create-speech`
- **Method**: POST
- **Parameters**:
  - `text` (str): The text to be converted into speech.
- **Response**: Generated audio from the provided text.

## Dependencies

- FastAPI
- Pydantic
- Uvicorn

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-service-api.git
   cd speech-service-api

2. Install the dependencies:
   ```bash
   pip install -r requirements.txt

3. Run the application:
   ```bash
    uvicorn main:app --reload



