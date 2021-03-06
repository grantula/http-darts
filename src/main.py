"""
Package: src
Filename: main.py
Author(s): Grant W
"""
# Python Imports

# Third Party Imports
from fastapi import FastAPI

# Local Imports
from db import db
from game.game import create_game
import endpoints

app = FastAPI()

# Get endpoints from our router
app.include_router(endpoints.router)

# Register a status endpoint
@app.get("/status")
async def status():
    return {"ding": "dong"}