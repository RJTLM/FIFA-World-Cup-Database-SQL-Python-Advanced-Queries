-- createLittleData.sql
CREATE TABLE LittleData (
    EventID INT PRIMARY KEY,
    EventYear INT,
    EventHost VARCHAR(255),
    NoTeams INT,
    Champion VARCHAR(255),
    RunnerUp VARCHAR(255),
    TopScorer VARCHAR(255),
    EventAttendance INT,
    EventAttendanceAvg INT,
    NoMatches INT
);
