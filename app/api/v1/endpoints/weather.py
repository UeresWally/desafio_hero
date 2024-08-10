from fastapi import APIRouter, HTTPException
from app.services.music_service import get_playlist
from app.services.weather_service import get_temperature
router = APIRouter()

@router.get("/playlist/")
async def get_playlist_by_city(city: str):
    try:
        temperature = await get_temperature(city)
        playlist = get_playlist(temperature)
        return {"city": city, "temperature": temperature, "playlist": playlist}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))