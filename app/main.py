from pathlib import Path

import requests
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"
app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
INDEX_HTML = BASE_DIR / "templates" / "index.html"

# Serve static files (favicon, assets)
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

FAV_SVG = BASE_DIR / "static" / "favicon.svg"


@app.get("/favicon.ico")
async def favicon():
    return FileResponse(FAV_SVG, media_type="image/x-icon")


@app.get("/")
async def home():
    return FileResponse(INDEX_HTML)


@app.get("/temperatura-cidade")
def temperatura_cidade(nome_cidade: str):
    geo_params = {
    "name": nome_cidade,
    "count": 1
    }
    geo_response = requests.get(GEO_URL, params=geo_params)
    geo_data = geo_response.json()
    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]
    weather_params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    weather_response = requests.get(WEATHER_URL, params=weather_params)
    weather_data = weather_response.json()
    return weather_data["current_weather"]["temperature"]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=1234,
        reload=True
    )