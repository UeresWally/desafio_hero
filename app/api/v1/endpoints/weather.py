from fastapi import APIRouter, HTTPException


router = APIRouter()

@router.get("/playlist/")
async def get_playlist_by_city(city: str):
    try:
        temperature = 15.0
        playlist = ['Faint', 'Lonely day', 'Sultans of swing', 'Foxy Lady']
        return {"city": city, "temperature": temperature, "playlist": playlist}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))