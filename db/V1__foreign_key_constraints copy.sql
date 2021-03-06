-- FK for games_players
ALTER TABLE f_game_player
ADD FOREIGN KEY (user_id) REFERENCES d_user(id);
ALTER TABLE f_game_player
ADD FOREIGN KEY (game_id) REFERENCES f_game(id);

-- FK for games
ALTER TABLE f_game
ADD FOREIGN KEY (game_type_id) REFERENCES d_game_type(id);

-- FK for game_move
ALTER TABLE f_game_move
ADD FOREIGN KEY (game_id) REFERENCES f_game(id);
ALTER TABLE f_game_move
ADD FOREIGN KEY (game_player_id) REFERENCES f_game_player(id);