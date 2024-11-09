import os
from dotenv import load_dotenv
load_dotenv()
class Config:
    API_URL = os.getenv("API_URL","")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY","")

config = Config()