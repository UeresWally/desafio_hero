from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str
    WEATHER_API_KEY: str

    class ConfigDict:
        env_file = ".env"

settings = Settings()