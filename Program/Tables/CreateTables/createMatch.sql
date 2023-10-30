/* createMatch.sql: MySQL file for creating the Match table */

-- Q3. Part2a. Implementation:
-- Create Match table with constraints
CREATE TABLE IF NOT EXISTS Match (
  MatchID INT PRIMARY KEY,
  Date DATE NOT NULL,
  HomeTeam VARCHAR(255),
  AwayTeam VARCHAR(255),
  HomeScore INT,
  AwayScore INT,
  Attendance INT,
  VenueName VARCHAR(255),
  Round VARCHAR(255) NOT NULL,
  Notes VARCHAR(255),
  FOREIGN KEY (HomeTeam) REFERENCES Team(TeamName) ON DELETE CASCADE,
  FOREIGN KEY (AwayTeam) REFERENCES Team(TeamName) ON DELETE CASCADE,
  FOREIGN KEY (VenueName) REFERENCES Venue(VenueName) ON DELETE SET NULL
);
