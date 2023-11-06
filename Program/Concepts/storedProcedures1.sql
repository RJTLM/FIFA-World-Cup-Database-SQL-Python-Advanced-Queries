/* storedProcedures1.sql: MySQL file for stored procedures */

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
