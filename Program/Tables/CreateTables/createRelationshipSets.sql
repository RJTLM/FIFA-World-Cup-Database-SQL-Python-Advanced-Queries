/* createRelationshipSets.sql: MySQL file for creating the relationship sets tables */

-- Q3. Part2a. Implementation:
-- Creating Plays Table (Many-to-Many Relationship)
CREATE TABLE Plays (
    MatchID INT,
    TeamName VARCHAR(255),
    PRIMARY KEY (MatchID, TeamName),
    FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeamName) REFERENCES Team(TeamName) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creating Manages Table (Many-to-Many Relationship)
CREATE TABLE Manages (
    MatchID INT,
    ManagerName VARCHAR(255),
    PRIMARY KEY (MatchID, ManagerName),
    FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ManagerName) REFERENCES Manager(ManagerName) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creating Captains Table (Many-to-Many Relationship)
CREATE TABLE Captains (
    MatchID INT,
    CaptainName VARCHAR(255),
    PRIMARY KEY (MatchID, CaptainName),
    FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (CaptainName) REFERENCES Captain(CaptainName) ON DELETE CASCADE ON UPDATE CASCADE
);
