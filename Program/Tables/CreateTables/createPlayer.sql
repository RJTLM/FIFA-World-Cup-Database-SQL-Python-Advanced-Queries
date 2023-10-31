/* createPlayer.sql: MySQL file for creating the Player table */

-- Q3. Part2a. Implementation:
-- Create Player table with constraints
CREATE TABLE IF NOT EXISTS Player (
  PlayerName VARCHAR(255) PRIMARY KEY,
  TeamName VARCHAR(255),
  FOREIGN KEY (TeamName) REFERENCES Team(TeamName) ON DELETE CASCADE
);

-- Add foreign key now both Team and Player tables have been created
ALTER TABLE Team
ADD FOREIGN KEY (Captain) REFERENCES Player(PlayerName) ON DELETE SET NULL;
