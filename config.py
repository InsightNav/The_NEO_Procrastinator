import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")

BASE_URL = "https://api.nasa.gov/neo/rest/v1/feed"
CACHE_DIR = "cache"