import openai
from .config import settings

openai.api_key = settings.AI_SECRET_KEY


def chat_gpt(message):
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "شما یک دستیار دوست داشتنی و مهربان هستید"},
            {"role": "user", "content": message},
        ],
    )
    
    return response