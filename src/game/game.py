"""
"""

# from sqlalchemy import text

from db import db

# Static rules for now
RULES = {
    # Which Values Are Needed (21=Bull)
    "values": [15, 16, 17, 18, 19, 20, 21],
    # How Many Times
    "occurrence": 3,
    # In Order? (False, Ascending, Descending) tbd
    "order": False
}

def get_last_insert_id(db_result):
    """
    """
    return db_result.context.cursor._last_insert_id

def create_game():
    print('hello')
    q = \
    """
    INSERT INTO f_game (
        game_type_id,
        status
    ) 
    VALUES (
        1,
        'in_progress'
    );
    """
    res = db.execute_raw(q) 
    game_id = get_last_insert_id(res)
    return {'game_id': game_id}

def check_winners(game_moves):
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