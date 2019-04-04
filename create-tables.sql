-- Remove old tables
DROP TABLE IF EXISTS games, users;

-- Game Data
CREATE TABLE rounds (
	round_id	serial PRIMARY KEY,
	prev_round	int REFERENCES rounds ON DELETE CASCADE,
	p1-choice	int,
	p2-choice	int,
);
CREATE TABLE games (
	game_id			serial PRIMARY KEY,
	current_round	int REFERENCES rounds ON DELETE CASCADE,
	-- player 1 stats
	p1-score		int DEFAULT 0,
	p1-done			boolean DEFAULT FALSE,
	-- player 2 stats
	p2-score		int DEFAULT 0,
	p2-done			boolean DEFAULT FALSE,
);
-- User Tables
CREATE TABLE users (
	user_id			serial PRIMARY KEY,
	wins			int,
	losses			int,
	current_game	int REFERENCES games,
	current_p1		boolean,
	longest_game	int REFERENCES games,
);
-- Login Tables?
