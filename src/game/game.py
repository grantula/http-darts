"""
"""

# from sqlalchemy import text

from db import db

def get_last_insert_id(db_result):
    """
    """
    return db_result.context.cursor._last_insert_id

def create_game():
    print('hello')
    # return {"hello": "hello"}
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