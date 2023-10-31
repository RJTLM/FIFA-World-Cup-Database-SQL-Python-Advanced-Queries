/* createSubstitution.sql: MySQL file for creating the Substitution table */

-- Q3. Part2a. Implementation:
-- Create Substitution table with constraints
CREATE TABLE IF NOT EXISTS Substitution (
  SubstitutionID INT PRIMARY KEY,
  MatchID INT,
  Time INT NOT NULL,
  PlayerOut VARCHAR(255),
  PlayerIn VARCHAR(255),
  TeamName VARCHAR(255),
  FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE,
  FOREIGN KEY (PlayerOut) REFERENCES Player(PlayerName) ON DELETE CASCADE,
  FOREIGN KEY (PlayerIn) REFERENCES Player(PlayerName) ON DELETE CASCADE,
  FOREIGN KEY (TeamName) REFERENCES Team(TeamName) ON DELETE CASCADE
);
