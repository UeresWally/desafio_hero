import httpx
from app.core.config import settings

async def get_temperature(city: str) -> float:
    api_key = settings.WEATHER_API_KEY
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={api_key}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response_data = response.json()

        if response.status_code != 200:
            raise Exception("City not found")
        return response_data['main']['temp']
    