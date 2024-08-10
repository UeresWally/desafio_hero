from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SPOTIFY_CLIENT_ID: str
    SPOTIFY_CLIENT_SECRET: str

    class ConfigDict:
        env_file = ".env"

settings = Settings()