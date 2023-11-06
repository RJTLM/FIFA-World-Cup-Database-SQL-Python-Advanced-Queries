/* storedProcedures.sql: MySQL file for stored procedures */

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
