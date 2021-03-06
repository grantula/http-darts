"""

"""

class GamesCollectionEndpoint:

    uri = '/v1/games'

    async def get():
        """View all games"""
        return {}

    async def post():
        """Create new game"""
        return {}


class GamesResourceEndpoint:

    uri = '/v1/games/{game_id:int}'

    async def get(game_id):
        """Get singular game"""
        return {"method": "get", "game_id": game_id}

    async def put(game_id):
        """Update game"""
        return {"method": "put", "game_id": game_id}

    async def delete(game_id):
        """Mark as canceled if exists"""
        return {"method": "delete", "game_id": game_id}