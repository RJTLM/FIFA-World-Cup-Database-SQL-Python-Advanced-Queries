/* advancedQueries.sql: MySQL file for advanced queries*/

-- Q3. Part3 Level 2 Advanced Queries:
-- Find the total number of matches played by each team
SELECT TeamName, COUNT(*) as TotalMatches FROM Plays GROUP BY TeamName ORDER BY TotalMatches DESC;

-- Get the average attendance of matches for each venue
SELECT Venue, AVG(Attendance) as AvgAttendance FROM FootballMatch WHERE Attendance IS NOT NULL GROUP BY Venue ORDER BY AvgAttendance DESC;

-- Find the top scorer of each event
SELECT EventID, TopScorer FROM Event WHERE TopScorer IS NOT NULL;

-- Get the total number of goals scored in each round of the 2023 event
SELECT Round, SUM(home_score + away_score) as TotalGoals FROM FootballMatch WHERE EventID = 9 GROUP BY Round ORDER BY TotalGoals DESC;

-- Find all matches where penalty kicks were taken in the 2023 event
SELECT FM.* FROM FootballMatch FM JOIN Event E ON FM.EventID = E.EventID WHERE (home_penalty IS NOT NULL OR away_penalty IS NOT NULL) AND E.EventYear = 2023;
