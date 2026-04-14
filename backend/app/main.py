from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.api import calendar
import os

origins_str = os.getenv("CORS_ORIGINS", "")
origins = origins_str.split(",") if origins_str else []

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


app.include_router(calendar.router)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
