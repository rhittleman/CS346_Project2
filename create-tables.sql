-- Remove old tables
DROP TABLE IF EXISTS logins, users, games, rounds;

-- Game Data
CREATE TABLE rounds (
	round_id	serial PRIMARY KEY,
	prev_round	int REFERENCES rounds ON DELETE CASCADE,
	p1_choice	int,
	p2_choice	int
);
CREATE TABLE games (
	game_id			serial PRIMARY KEY,
	current_round	int REFERENCES rounds ON DELETE CASCADE,
	-- player 1 stats
	p1_score		int DEFAULT 0,
	p1_done			boolean DEFAULT FALSE,
	-- player 2 stats
	p2_score		int DEFAULT 0,
	p2_done			boolean DEFAULT FALSE
);
-- User Tables
CREATE TABLE users (
	user_id			serial PRIMARY KEY,
	wins			int,
	losses			int,
	current_game	int REFERENCES games,
	current_p1		boolean
);
-- Login Tables?
CREATE TABLE logins (
	username		varchar,
	password		varchar,
	user_id			int REFERENCES users ON DELETE CASCADE,
	PRIMARY KEY (username, password)
);
