/* ./Program/Tables/createTablesWithoutFKDep.sql: MySQL file for creating the tables without foreign key dependencies */

-- Q3. Part2a. Implementation:
-- Creating Team Table
CREATE TABLE IF NOT EXISTS Team (
    TeamName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Player Table
CREATE TABLE IF NOT EXISTS Player (
    PlayerName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE,
    isCaptain BOOLEAN DEFAULT FALSE
);

-- Creating Manager Table
CREATE TABLE IF NOT EXISTS Manager (
    ManagerName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Referee Table
CREATE TABLE IF NOT EXISTS Referee (
    RefereeName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Event Table
CREATE TABLE IF NOT EXISTS Event (
    EventID INT PRIMARY KEY NOT NULL UNIQUE,
    EventYear YEAR,
    EventHost VARCHAR(255),
    NoTeams INT,
    Champion VARCHAR(255),
    RunnerUp VARCHAR(255),
    TopScorer VARCHAR(255),
    EventAttendance INT,
    EventAttendanceAvg FLOAT,
    NoMatches INT
);
