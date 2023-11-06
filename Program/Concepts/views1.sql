/* views1.sql: MySQL file for views */

-- View for match attendance summary
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-view.html
CREATE VIEW ViewMatchAttendanceSummary AS
SELECT Venue, AVG(Attendance) as AvgAttendance
FROM FootballMatch
WHERE Attendance IS NOT NULL
GROUP BY Venue;
