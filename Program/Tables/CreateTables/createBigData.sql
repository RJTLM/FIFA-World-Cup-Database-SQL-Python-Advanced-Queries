-- createBigData.sql
CREATE TABLE BigData (
    MatchID INT PRIMARY KEY,
    home_team VARCHAR(255),
    away_team VARCHAR(255),
    home_score INT,
    home_penalty INT,
    away_score INT,
    away_penalty INT,
    home_manager VARCHAR(255),
    home_captain VARCHAR(255),
    away_manager VARCHAR(255),
    away_captain VARCHAR(255),
    MatchAttendance INT,
    Venue VARCHAR(255),
    Round VARCHAR(255),
    MatchDate DATE,
    Referee VARCHAR(255),
    Notes TEXT,
    MatchHost VARCHAR(255),
    MatchYear INT
);
