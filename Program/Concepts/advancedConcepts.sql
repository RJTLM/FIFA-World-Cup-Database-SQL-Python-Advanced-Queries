/* advancedConcepts.sql: MySQL file for advanced concepts and functionality */

-- Stored Procedures
-- Procedure to get total matches by team
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-procedure.html
CREATE PROCEDURE GetTotalMatchesByTeam(IN teamName VARCHAR(255))
BEGIN
    SELECT TeamName, COUNT(*) as TotalMatches 
    FROM Plays 
    WHERE TeamName = teamName
    GROUP BY TeamName;
END;
-- How to call: CALL GetTotalMatchesByTeam('USA');

-- Procedure to get average attendance by year
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/group-by-functions.html#function_avg
CREATE PROCEDURE GetAverageAttendanceByYear(IN year INT)
BEGIN
    SELECT Venue, AVG(Attendance) as AvgAttendance 
    FROM FootballMatch 
    WHERE YEAR(MatchDate) = year AND Attendance IS NOT NULL 
    GROUP BY Venue;
END;
-- How to call: CALL GetAverageAttendanceByYear(2023);

-- Triggers
-- Trigger before insert on FootballMatch to check for unusually high attendance
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-trigger.html
CREATE TRIGGER BeforeInsertFootballMatch
BEFORE INSERT ON FootballMatch
FOR EACH ROW
BEGIN
    IF NEW.Attendance > (SELECT AVG(Attendance) * 1.5 FROM FootballMatch) THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Attendance is unusually high.';
    END IF;
END;

-- Trigger after update on Event to log changes in top scorer
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/trigger-syntax.html
CREATE TRIGGER AfterUpdateEvent
AFTER UPDATE ON Event
FOR EACH ROW
BEGIN
    IF OLD.TopScorer <> NEW.TopScorer THEN
        INSERT INTO EventLog(EventID, ChangeDescription)
        VALUES (NEW.EventID, CONCAT('Top scorer changed from ', OLD.TopScorer, ' to ', NEW.TopScorer));
    END IF;
END;

-- Views
-- View for top scorers
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-view.html
/*CREATE VIEW ViewTopScorers AS
SELECT EventID, TopScorer
FROM Event
WHERE TopScorer IS NOT NULL;*/

-- View for match attendance summary
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-view.html
CREATE VIEW ViewMatchAttendanceSummary AS
SELECT Venue, AVG(Attendance) as AvgAttendance
FROM FootballMatch
WHERE Attendance IS NOT NULL
GROUP BY Venue;

-- Indexes
-- Index on TeamName in Plays Table to improve search performance
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-index.html
CREATE INDEX idx_teamname ON Plays(TeamName);

-- Index on MatchDate and Attendance in FootballMatch Table to improve query performance
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-index.html
CREATE INDEX idx_date_attendance ON FootballMatch(MatchDate, Attendance);

-- To demonstrate improved performance:
-- Query without index: EXPLAIN SELECT * FROM Plays WHERE TeamName = 'USA';
-- Query with index: EXPLAIN SELECT * FROM Plays USE INDEX (idx_teamname) WHERE TeamName = 'USA';
-- Query using the index should have a lower row scan count, indicating a more efficient query execution.
-- Reference for EXPLAIN: https://dev.mysql.com/doc/refman/8.0/en/explain.html
