/* createTablesWithoutFKDep.sql: MySQL file for creating the tables without foreign key dependencies */

-- Q3. Part2a. Implementation:
-- Creating Team Table
CREATE TABLE Team (
    TeamName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Player Table
CREATE TABLE Player (
    PlayerName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Manager Table
CREATE TABLE Manager (
    ManagerName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Captain Table
CREATE TABLE Captain (
    CaptainName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Referee Table
CREATE TABLE Referee (
    RefereeName VARCHAR(255) PRIMARY KEY NOT NULL UNIQUE
);

-- Creating Event Table
CREATE TABLE Event (
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
