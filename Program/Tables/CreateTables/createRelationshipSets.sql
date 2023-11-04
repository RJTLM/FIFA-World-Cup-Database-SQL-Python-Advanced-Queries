/* ./Program/Tables/createRelationshipSets.sql: MySQL file for creating the relationship sets tables */

-- Q3. Part2a. Implementation:
-- Creating Plays Table (Many-to-Many Relationship)
CREATE TABLE IF NOT EXISTS Plays (
    MatchID INT,
    TeamName VARCHAR(255),
    HomeAway ENUM('Home', 'Away') NOT NULL,
    PRIMARY KEY (MatchID, TeamName),
    FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (TeamName) REFERENCES Team(TeamName) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Creating Manages Table (Many-to-Many Relationship)
CREATE TABLE IF NOT EXISTS Manages (
    MatchID INT,
    ManagerName VARCHAR(255),
    PRIMARY KEY (MatchID, ManagerName),
    FOREIGN KEY (MatchID) REFERENCES FootballMatch(MatchID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (ManagerName) REFERENCES Manager(ManagerName) ON DELETE CASCADE ON UPDATE CASCADE
);
