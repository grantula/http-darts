"""

"""

from db import db
from sqlalchemy import text
from pydantic import BaseModel
from fastapi import HTTPException
from exceptions import HTTPNotImplementedException

class User(BaseModel):
    name: str


class UsersCollectionEndpoint:

    uri = '/v1/users'

    async def get():
        q = text("SELECT * FROM d_user")
        res = db.execute_query(q)
        """View all users"""
        return res

    async def post(user: User):
        """Create new user"""
        q = text(
            """
            INSERT INTO d_user (name) VALUES (:user_name)
            """
        )
        params = {'user_name': user.name}
        user_id = db.perform_insert(q, params)
        return {"user_id": user_id}


class UsersResourceEndpoint:

    uri = '/v1/users/{user_id:int}'

    async def get(user_id):
        """Get singular user"""
        q = text(
            """SELECT * FROM d_user WHERE id = :user_id"""
        )
        params = {'user_id': user_id}
        res = db.execute_query(q, params)
        return res

    async def put(user_id):
        """Update user"""
        raise HTTPNotImplementedException

    async def delete(user_id):
        """Mark as inactive if exists"""
        raise HTTPNotImplementedException