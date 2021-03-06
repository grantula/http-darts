"""

"""

class GameMovesCollectionEndpoint:

    uri = '/v1/games/{game_id:int}/moves'

    async def get(game_id):
        """View all game_moves"""
        return {"game_id": game_id}

    async def post(game_id):
        """Create new game_move"""
        return {"game_id": game_id}


class GameMovesResourceEndpoint:

    uri = '/v1/games/{game_id:int}/moves/{move_id:int}'

    async def get(game_id, move_id):
        """Get singular game_move"""
        return {"method": "get", "game_id": game_id, "move_id": move_id}

    async def put(game_id, move_id):
        """Update game_move"""
        return {"method": "put", "game_id": game_id, "move_id": move_id}

    async def delete(game_id, move_id):
        """Mark as inactive if exists"""
        return {"method": "delete", "game_id": game_id, "move_id": move_id}