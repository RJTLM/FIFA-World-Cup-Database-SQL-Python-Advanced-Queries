/* createWinner.sql: MySQL file for creating the Winner table */

-- Q3. Part2a. Implementation:
-- Create Winner table
CREATE TABLE IF NOT EXISTS Winner (
  MatchID INT PRIMARY KEY,
  FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE
);
