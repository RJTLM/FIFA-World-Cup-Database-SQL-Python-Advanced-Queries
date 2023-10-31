/* createTeamCaptain.sql: MySQL file for creating the Team Captain table */
/* This table exists to eliminate circular dependency between Team and Player */

-- Q3. Part2a. Implementation:
-- Create Team Captain table with constraints
CREATE TABLE IF NOT EXISTS TeamCaptain (
  TeamName VARCHAR(255),
  PlayerName VARCHAR(255) UNIQUE,
  PRIMARY KEY (TeamName),
  FOREIGN KEY (TeamName) REFERENCES Team(TeamName) ON DELETE CASCADE,
  FOREIGN KEY (PlayerName) REFERENCES Player(PlayerName) ON DELETE SET NULL
);
