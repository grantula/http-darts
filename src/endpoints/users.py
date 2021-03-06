"""

"""

class UsersCollectionEndpoint:

    uri = '/v1/users'

    async def get():
        """View all users"""
        return {}

    async def post():
        """Create new user"""
        return {}


class UsersResourceEndpoint:

    uri = '/v1/users/{user_id:int}'

    async def get(game_id):
        """Get singular user"""
        return {"method": "get", "user_id": user_id}

    async def put(game_id):
        """Update user"""
        return {"method": "put", "user_id": user_id}

    async def delete(game_id):
        """Mark as inactive if exists"""
        return {"method": "delete", "user_id": user_id}