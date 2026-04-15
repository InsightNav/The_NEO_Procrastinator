import os
import json
import random
from datetime import datetime

import requests

from config import API_KEY, BASE_URL, CACHE_DIR


LUNAR_DISTANCE_KM = 384400


def today_str() -> str:
    """Return today's date as YYYY-MM-DD."""
    return datetime.today().strftime("%Y-%m-%d")


# ---------- Cache ---------- #

def get_cache_file() -> str:
    return os.path.join(CACHE_DIR, f"{today_str()}.json")


def load_cache():
    """Load cached API response if available."""
    path = get_cache_file()
    if os.path.exists(path):
        with open(path, "r") as f:
            return json.load(f)
    return None


def save_cache(data) -> None:
    """Save API response to cache."""
    os.makedirs(CACHE_DIR, exist_ok=True)
    with open(get_cache_file(), "w") as f:
        json.dump(data, f)


# ---------- Fetch ---------- #

def fetch_data(force_refresh: bool = False):
    """Fetch asteroid data from NASA API with caching."""
    if not force_refresh:
        cached = load_cache()
        if cached:
            return cached

    params = {
        "start_date": today_str(),
        "end_date": today_str(),
        "api_key": API_KEY,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
    except requests.RequestException as e:
        print(f"API error: {e}")

        cached = load_cache()
        if cached:
            print("Using cached data.")
            return cached

        raise

    save_cache(data)
    return data


# ---------- Processing ---------- #

def extract_metrics(data):
    """Extract key asteroid metrics."""
    try:
        asteroids = data["near_earth_objects"][today_str()]
    except KeyError:
        raise ValueError("Unexpected API response format")

    asteroid_count = len(asteroids)
    max_diameter = 0
    min_distance = float("inf")
    hazardous = False

    for asteroid in asteroids:
        diameter = asteroid["estimated_diameter"]["meters"]["estimated_diameter_max"]

        distance_km = float(
            asteroid["close_approach_data"][0]["miss_distance"]["kilometers"]
        )
        distance_ld = distance_km / LUNAR_DISTANCE_KM

        max_diameter = max(max_diameter, diameter)
        min_distance = min(min_distance, distance_ld)

        if asteroid["is_potentially_hazardous_asteroid"]:
            hazardous = True

    return asteroid_count, max_diameter, min_distance, hazardous


# ---------- Urgency Logic ---------- #

def get_urgency(distance: float, diameter: float, hazardous: bool):
    """Determine urgency level and message."""

    if hazardous:
        messages = [
            "A dangerous object is nearby. Today is officially optional.",
            "Space is getting aggressive. Cancel plans and enjoy existence.",
            "Potentially hazardous asteroid detected. Productivity is now a myth.",
            "This feels like a good day to ignore responsibilities entirely.",
        ]
        return 3, random.choice(messages)

    if distance < 10 or diameter > 500:
        messages = [
            "Cosmic activity detected. Keep things minimal today.",
            "Asteroids are unusually close. Do less, think less.",
            "Space is active. You are allowed to lower expectations.",
            "The universe is busy. You don't need to be.",
        ]
        return 2, random.choice(messages)

    messages = [
        "Quiet skies. Unfortunately, responsibilities still exist.",
        "Space is calm. You have no cosmic excuse today.",
        "Nothing interesting in space. It's all on you now.",
        "The universe is silent. Your to-do list is not.",
    ]
    return 1, random.choice(messages)