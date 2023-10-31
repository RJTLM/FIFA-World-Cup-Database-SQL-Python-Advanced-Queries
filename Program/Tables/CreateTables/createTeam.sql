/* createTeam.sql: MySQL file for creating the Team table */

-- Q3. Part2a. Implementation:
-- Create Team table with constraints
CREATE TABLE IF NOT EXISTS Team (
  TeamName VARCHAR(255) PRIMARY KEY,
  Manager VARCHAR(255) UNIQUE,
  Captain VARCHAR(255) UNIQUE,
  FOREIGN KEY (Manager) REFERENCES Coach(CoachName) ON DELETE SET NULL,
  FOREIGN KEY (Captain) REFERENCES Player(PlayerName) ON DELETE SET NULL
);
