from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

client = OpenAI(
    api_key=my_key_openai
)

def transcribe_with_whisper(audio_file_name):

    audio_file = open(audio_file_name, "rb")

    AI_generated_trancript = client.audio.transcription.create(
        model="whisper-1",
        file=audio_file,
        language="tr"
    )

    return AI_generated_trancript.text