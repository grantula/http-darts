"""

"""

class GamePlayersCollectionEndpoint:

    uri = '/v1/games/{game_id:int}/players'

    async def get(game_id):
        """View all game_players"""
        return {"game_id": game_id}

    async def post(game_id):
        """Create new game_player"""
        return {"game_id": game_id}


class GamePlayersResourceEndpoint:

    uri = '/v1/games/{game_id:int}/players/{player_id:int}'

    async def get(game_id, player_id):
        """Get singular game_player"""
        return {"method": "get", "game_id": game_id, "player_id": player_id}

    async def put(game_id, player_id):
        """Update game_player"""
        return {"method": "put", "game_id": game_id, "player_id": player_id}

    async def delete(game_id, player_id):
        """Mark as inactive if exists"""
        return {"method": "delete", "game_id": game_id, "player_id": player_id}