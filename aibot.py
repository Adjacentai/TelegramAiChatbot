import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API = os.getenv("OPENAI_API")
MODEL_URL = os.getenv("MODEL_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

# Setting up a client to connect to a local AI server
client = OpenAI(
    base_url=MODEL_URL,  # Address of the local server with the AI model
    api_key=OPENAI_API  # Local access key
)

def send_to_aibot(messages):
    completion = client.chat.completions.create(
        model=MODEL_NAME,  # Name of the language model on the local server
        messages=messages,
        temperature=0.7,  # Creativity parameter
    )

    return completion.choices[0].message.content
