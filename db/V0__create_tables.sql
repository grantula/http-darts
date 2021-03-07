
-- Table for users
CREATE TABLE IF NOT EXISTS
d_user (
   id          INT       NOT NULL AUTO_INCREMENT,
   name        TEXT      NOT NULL,
   create_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   update_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (id)
);

-- Table for game types
CREATE TABLE IF NOT EXISTS
d_game_type (
   id          INT       NOT NULL AUTO_INCREMENT,
   name        TEXT      NOT NULL,
   create_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   update_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (id)
);

-- table for games_players
CREATE TABLE IF NOT EXISTS
f_game_player (
   id          INT       NOT NULL AUTO_INCREMENT,
   user_id     INT       NOT NULL,
   game_id     INT       NOT NULL,
   PRIMARY KEY (id)
);

-- Table for games
CREATE TABLE IF NOT EXISTS
f_game (
   id           INT       NOT NULL AUTO_INCREMENT,
   game_type_id INT       NOT NULL,
   status       ENUM      ('created', 'in_progress', 'complete', 'canceled'),
   winner       INT       DEFAULT NULL,
   create_date  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   update_date  TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (id)
);

-- Table for game_moves
CREATE TABLE IF NOT EXISTS
f_game_move (
   id              INT       NOT NULL AUTO_INCREMENT,
   game_id         INT       NOT NULL,
   game_player_id  INT       NOT NULL,
   number          INT(2)    DEFAULT 0,
   modifier        INT(1)    DEFAULT 1,
   winner          INT       DEFAULT NULL,
   create_date     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   update_date     TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY (id),
   CONSTRAINT  number_ck   CHECK (number IN (0, 15, 16, 17, 18, 19, 20)),
   CONSTRAINT  modifier_ck CHECK (modifier IN (1, 2, 3))
);