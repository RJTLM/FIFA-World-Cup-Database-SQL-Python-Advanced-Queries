/* createGoal.sql: MySQL file for creating the Goal table */

-- Q3. Part2a. Implementation:
-- Create Goal table with constraints
CREATE TABLE IF NOT EXISTS Goal (
  GoalID INT AUTO_INCREMENT PRIMARY KEY, -- https://www.w3schools.com/mysql/mysql_autoincrement.asp
  MatchID INT,
  ScoringTeam VARCHAR(255),
  Scorer VARCHAR(255),
  Assist VARCHAR(255),
  Time INT NOT NULL,
  Type VARCHAR(255) NOT NULL,
  FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE,
  FOREIGN KEY (ScoringTeam) REFERENCES Team(TeamName) ON DELETE CASCADE,
  FOREIGN KEY (Scorer) REFERENCES Player(PlayerName) ON DELETE CASCADE,
  FOREIGN KEY (Assist) REFERENCES Player(PlayerName) ON DELETE CASCADE
);
