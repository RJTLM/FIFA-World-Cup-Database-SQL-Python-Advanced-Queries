/* createCard.sql: MySQL file for creating the Card table */

-- Q3. Part2a. Implementation:
-- Create Card table with constraints
CREATE TABLE IF NOT EXISTS Card (
  CardID INT PRIMARY KEY,
  MatchID INT,
  Time INT NOT NULL,
  Type VARCHAR(255) NOT NULL,
  TeamName VARCHAR(255),
  PlayerName VARCHAR(255),
  FOREIGN KEY (MatchID) REFERENCES Match(MatchID) ON DELETE CASCADE,
  FOREIGN KEY (TeamName) REFERENCES Team(TeamName) ON DELETE CASCADE,
  FOREIGN KEY (PlayerName) REFERENCES Player(PlayerName) ON DELETE CASCADE
);
