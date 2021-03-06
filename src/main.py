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

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/select_one")
async def select_one():
    """ testing db """
    res = db.select_one()
    return {"message": res}
