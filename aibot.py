import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
OPENAI_API = os.getenv("OPENAI_API")
MODEL_URL = os.getenv("MODEL_URL")
MODEL_NAME = os.getenv("MODEL_NAME")

# Настройка клиента для подключения к локальному серверу AI
client = OpenAI(
    base_url=MODEL_URL,  # Адрес локального сервера с AI-моделью
    api_key=OPENAI_API  # Локальный ключ доступа
)

def send_to_aibot(messages):
    completion = client.chat.completions.create(
        model=MODEL_NAME,  # Название языковой модели на локальном сервере
        messages=messages,
        temperature=0.7,  # Параметр креативности
    )

    return completion.choices[0].message.content
