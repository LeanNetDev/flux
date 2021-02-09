# Intended to be a simple method of exposing the features implemented in development environments to clients
from typing import Optional

from fastapi import FastAPI

app = FastAPI()

from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

from modules.services import get_devices

@app.get("/")
def read_root():
    devices = get_devices()
    return devices


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}