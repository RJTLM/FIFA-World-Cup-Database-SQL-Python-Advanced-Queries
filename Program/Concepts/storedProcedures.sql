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
