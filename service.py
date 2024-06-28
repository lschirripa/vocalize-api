import sounddevice as sd
from scipy.io.wavfile import write
from pydub import AudioSegment
import time
import pygame
from pathlib import Path
from openai import OpenAI

client = OpenAI()


class VocalizeService:
    def __init__(self):
        pass

    def record_audio(self, duration, filename):
        fs = 44100
        print("Recording...")
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
        sd.wait()
        print("Recording finished")

        wav_filename = filename + '.wav'
        write(wav_filename, fs, recording)

        audio = AudioSegment.from_wav(wav_filename)
        mp3_filename = filename + '.mp3'
        audio.export(mp3_filename, format="mp3")
        print(f"Audio saved as {mp3_filename}")

    def audio_to_text(self, audio_file) -> str:
        transcript = client.audio.transcriptions.create(
            file=audio_file,
            model="whisper-1",
            response_format="text",
        )
        print(transcript)
        return transcript

    def generate_corrected_transcript(self) -> str: #todo could be useful to use prompts for getting specific orders
        system_prompt = "You are a helpful assistant. Your task is to correct any spelling discrepancies in the transcribed text. The output should be the text corrected. Return the same text if there were no errors"
        audio_file = open("output.mp3", "rb")
        temperature = 0

        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=temperature,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": self.audio_to_text(audio_file)
                }
            ]
        )
        return response.choices[0].message.content

    def create_transcription(self, duration) -> str:
        self.record_audio(duration, 'output')
        corrected_text = self.generate_corrected_transcript()
        return corrected_text

    def text_to_speech(self, text):
        self.create_audio(text)
        self.reproduce_voice()

    def create_audio(self, text):
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=text
        )
        response.stream_to_file(speech_file_path)

    def reproduce_voice(self):
        pygame.mixer.init()
        pygame.mixer.music.load("speech.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            time.sleep(1)
