"""
"""

# from sqlalchemy import text

# from db import db

# Static rules for now
RULES = {
    # Which Values Are Needed (21=Bull)
    "values": [15, 16, 17, 18, 19, 20, 21],
    # How Many Times
    "occurrence": 3,
    # In Order? (False, Ascending, Descending) tbd
    "order": False
}

class CannotAddPlayerWhileGameInProgressException(Exception):
    pass


class GameNotFoundException(Exception):
    pass


class Darts:

    STATUS_CREATED = 'created'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_CANCELED = 'canceled'
    STATUS_COMPLETE = 'complete'

    def __init__(self, db, game_id=None):
        self.db = db

        if game_id:
            self.load_from_game_id(game_id)

    def load_from_game_id(self, game_id):
        """Load our game given an ID
        """
        self.info_game = self.get_game(game_id)
        self.info_game_players = self.get_players(game_id)
        self.info_game_moves = self.get_moves(game_id)

    def add_game(self):
        """Create a game in the database""" 
        q = \
        f"""
        INSERT INTO f_game (
            game_type_id,
            status
        ) 
        VALUES (
            1,
            :status
        );
        """
        params = {"status": STATUS_CREATED}
        self.game_id = self.db.perform_insert(q, params)
        self.game_status = STATUS_CREATED
        return {'game_id': self.game_id}
    
    def get_game(self, game_id)
        q = \
        """
        SELECT * 
        FROM f_game
        WHERE id = :game_id
        """
        params = {"game_id": game_id}
        game = self.db.execute_query(q, params)
        if not game:
            raise GameNotFoundException()
        return self.game
    
    def start_game(self, game_id):
        self.update_game_status(game_id, STATUS_IN_PROGRESS)
    
    def cancel_game(self, game_id):
        self.update_game_status(game_id, STATUS_CANCELED)

    def complete_game(self, game_id):
        self.update_game_status(game_id, STATUS_COMPLETE)

    def update_game_status(self, game_id, game_status):
        """move game status from start to in_progress"""
        q = \
        """
        UPDATE f_game
        SET status = :status
        WHERE game_id = :game_id
        """
        params = {"status": game_status, "game_id": game_id}
        status = self.db.execute_query(q, params)
        return status
    
    def get_players(self, game_id):
        q = \
        """
        SELECT * 
        FROM f_game_player
        WHERE game_id = :game_id
        """
        players = self.db.execute_query(q)
        return players

    def add_player(self, user_id, game_id):
        """Add player when game is in created state only"""
        if self.game_status != STATUS_CREATED:
            raise CannotAddPlayerWhileGameInProgressException()
        q = \
        """
        INSERT INTO f_game_player (
            user_id, 
            game_id
        )
        VALUES (:user_id, :game_id)
        """
        params = {"user_id": user_id, "game_id": game_id}
        game_player_id = self.db.perform_insert(q, params)
        return game_player_id

    def get_moves(self, game_id):
        """Get game moves from db"""
        q = \
        """
        SELECT * 
        FROM f_game_moves
        WHERE game_id = :game_id;
        """
        params = {"game_id": game_id}
        moves = self.db.execute_query(q, params)
        return moves

    def add_move(self, user_id, number, modifier):
        """Add a move for a player"""
        q = \
        """
        INSERT INTO f_game_move (
            number, 
            modifier,
            game_player_id
        )
        VALUES (
            :number, 
            :modifier, 
            (SELECT id 
             FROM f_game_player
             WHERE user_id = :user_id
             AND   game_id = :game_id))
        """
        params = {"number": number, 
                  "modifier": modifier, 
                  "user_id": user_id,
                  "game_id": game_id}
        game_move_id = self.db.perform_insert(q, params)
        return game_move_id

    def check_winners(self, game_moves):
        """
        first rev of winner algo, can certainly be improved
        game_moves = [{player_id, number, modifier, create_date}...]
        """
        game_moves = sorted(game_moves, key=lambda k: k['create_date'])
        to_win = sorted(RULES['values'] * RULES['occurrence'])
        scoreboard = {x['player_id']: to_win for x in game_moves}
        for move in game_moves:
            player_id = move['player_id']
            modifier = move['modifier']
            number = move['number']
            for n in range(modifier + 1):
                if number in scoreboard[player_id]:
                    scoreboard[player_id].remove(number)
            if not len(scoreboard[player_id]):
                return player_id
        return None