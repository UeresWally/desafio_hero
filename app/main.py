from fastapi import FastAPI
from app.api.v1.endpoints import weather

app = FastAPI()

app.include_router(weather.router, prefix="/api/v1")