from openai import OpenAI
from app.config import settings

def get_client():
    return OpenAI(api_key=settings.OPENAI_API_KEY)
