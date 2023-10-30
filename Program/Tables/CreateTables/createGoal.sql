/* createGoal.sql: MySQL file for creating the Goal table */

-- Q3. Part2a. Implementation:
-- Create Goal table with constraints
CREATE TABLE IF NOT EXISTS Goal (
  GoalID INT PRIMARY KEY,
  MatchID INT,
  ScoringTeam VARCHAR(255),
  Scorer VARCHAR(255),
  Assist VARCHAR(255),
  Time INT NOT NULL,
  Type VARCHAR(255) NOT NULL,
  FOREIGN KEY (MatchID) REFERENCES Match(MatchID) ON DELETE CASCADE,
  FOREIGN KEY (ScoringTeam) REFERENCES Team(TeamName) ON DELETE CASCADE,
  FOREIGN KEY (Scorer) REFERENCES Player(PlayerName) ON DELETE CASCADE,
  FOREIGN KEY (Assist) REFERENCES Player(PlayerName) ON DELETE CASCADE
);
