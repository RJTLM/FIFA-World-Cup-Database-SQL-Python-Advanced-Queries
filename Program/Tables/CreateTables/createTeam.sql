/* createTeam.sql: MySQL file for creating the Team table */

-- Q3. Part2a. Implementation:
-- Create Team table with constraints
CREATE TABLE IF NOT EXISTS Team (
  TeamName VARCHAR(255) PRIMARY KEY,
  CoachName VARCHAR(255) UNIQUE,
  FOREIGN KEY (CoachName) REFERENCES Coach(CoachName) ON DELETE SET NULL
);
