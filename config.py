import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
SLSKD_URL = os.getenv("SLSKD_URL")

HEADERS = {"X-API-Key": API_KEY, "Content-Type": "application/json"}
