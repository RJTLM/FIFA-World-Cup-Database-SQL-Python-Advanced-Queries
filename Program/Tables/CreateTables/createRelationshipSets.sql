/* createRelationshipSets.sql: MySQL file for creating the relationship sets tables */

-- Q3. Part2a. Implementation:
-- Create Hosts table with constraints
CREATE TABLE IF NOT EXISTS Hosts (
  CountryName VARCHAR(255),
  EventID INT,
  PRIMARY KEY (CountryName, EventID),
  FOREIGN KEY (CountryName) REFERENCES Country(CountryName) ON DELETE CASCADE,
  FOREIGN KEY (EventID) REFERENCES Event(EventID) ON DELETE CASCADE
);

-- Create PlayedAt table with constraints
CREATE TABLE IF NOT EXISTS PlayedAt (
  MatchID INT,
  VenueName VARCHAR(255),
  PRIMARY KEY (MatchID, VenueName),
  FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE,
  FOREIGN KEY (VenueName) REFERENCES Venue(VenueName) ON DELETE CASCADE
);

-- Create ParticipatesIn table with constraints
CREATE TABLE IF NOT EXISTS ParticipatesIn (
  PlayerName VARCHAR(255),
  EventID INT,
  PRIMARY KEY (PlayerName, EventID),
  FOREIGN KEY (PlayerName) REFERENCES Player(PlayerName) ON DELETE CASCADE,
  FOREIGN KEY (EventID) REFERENCES Event(EventID) ON DELETE CASCADE
);

-- Create OfficiatedBy table with constraints
CREATE TABLE IF NOT EXISTS OfficiatedBy (
  MatchID INT,
  OfficialName VARCHAR(255),
  PRIMARY KEY (MatchID, OfficialName),
  FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE,
  FOREIGN KEY (OfficialName) REFERENCES Official(OfficialName) ON DELETE CASCADE
);

-- Create ConsistsOf table with constraints
CREATE TABLE IF NOT EXISTS ConsistsOf (
  StageRound VARCHAR(255),
  MatchID INT,
  PRIMARY KEY (StageRound, MatchID),
  FOREIGN KEY (StageRound) REFERENCES Stage(Round) ON DELETE CASCADE,
  FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE
);
