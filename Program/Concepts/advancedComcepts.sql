/* advancedConcepts.sql: MySQL file for advanced concepts and functionality */

-- Stored Procedures
-- Procedure to get total matches by team
DELIMITER $$

CREATE PROCEDURE GetTotalMatchesByTeam(IN teamName VARCHAR(255))
BEGIN
    SELECT TeamName, COUNT(*) as TotalMatches 
    FROM Plays 
    WHERE TeamName = teamName
    GROUP BY TeamName;
END$$

DELIMITER ;
-- How to call: CALL GetTotalMatchesByTeam('USA');

DELIMITER $$

CREATE PROCEDURE GetAverageAttendanceByYear(IN year INT)
BEGIN
    SELECT Venue, AVG(Attendance) as AvgAttendance 
    FROM FootballMatch 
    WHERE YEAR(Date) = year AND Attendance IS NOT NULL 
    GROUP BY Venue;
END$$

DELIMITER ;
-- How to call: CALL GetAverageAttendanceByYear(2023);

-- Triggers
-- Trigger before insert on FootballMatch
DELIMITER $$

CREATE TRIGGER BeforeInsertFootballMatch
BEFORE INSERT ON FootballMatch
FOR EACH ROW
BEGIN
    IF NEW.Attendance > (SELECT AVG(Attendance) * 1.5 FROM FootballMatch) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Attendance is unusually high.';
    END IF;
END$$

DELIMITER ;

-- Trigger after update on Event
DELIMITER $$

CREATE TRIGGER AfterUpdateEvent
AFTER UPDATE ON Event
FOR EACH ROW
BEGIN
    IF OLD.TopScorer <> NEW.TopScorer THEN
        INSERT INTO EventLog(EventID, ChangeDescription)
        VALUES (NEW.EventID, CONCAT('Top scorer changed from ', OLD.TopScorer, ' to ', NEW.TopScorer));
    END IF;
END$$

DELIMITER ;

-- Views
-- View for top scorers
CREATE VIEW ViewTopScorers AS
SELECT EventID, TopScorer
FROM Event
WHERE TopScorer IS NOT NULL;

-- View for match attendance summary
CREATE VIEW ViewMatchAttendanceSummary AS
SELECT Venue, AVG(Attendance) as AvgAttendance
FROM FootballMatch
WHERE Attendance IS NOT NULL
GROUP BY Venue;

-- Indexes
-- Index on TeamName in Plays Table
CREATE INDEX idx_teamname ON Plays(TeamName);

-- Index on Date and Attendance in FootballMatch Table
CREATE INDEX idx_date_attendance ON FootballMatch(Date, Attendance);

-- To demonstrate improved performance:
-- Query without index: EXPLAIN SELECT * FROM Plays WHERE TeamName = 'USA';
-- Query with index: EXPLAIN SELECT * FROM Plays USE INDEX (idx_teamname) WHERE TeamName = 'USA';
-- Query using the index should have a lower row scan count, indicating a more efficient query execution.
