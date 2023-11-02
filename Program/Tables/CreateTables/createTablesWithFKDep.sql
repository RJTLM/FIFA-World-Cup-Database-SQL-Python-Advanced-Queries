/* createTablesWithFKDep.sql: MySQL file for creating the tables with foreign key dependencies */

-- Q3. Part2a. Implementation:
-- Creating FootballMatch Table
CREATE TABLE FootballMatch (
    MatchID INT PRIMARY KEY NOT NULL UNIQUE,
    home_score INT,
    away_score INT,
    home_penalty INT,
    away_penalty INT,
    Attendance INT,
    Venue VARCHAR(255),
    Round VARCHAR(50),
    MatchDate DATE,
    Notes TEXT,
    MatchHost VARCHAR(255),
    EventID INT,
    RefereeName VARCHAR(255),
    FOREIGN KEY (EventID) REFERENCES Event(EventID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (RefereeName) REFERENCES Referee(RefereeName) ON DELETE SET NULL ON UPDATE CASCADE
);
