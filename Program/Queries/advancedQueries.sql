/* advancedQueries.sql: MySQL file for advanced queries*/

-- Q3. Part3 Level 2 Advanced Queries:
-- advancedQueries.sql: MySQL file for advanced queries

-- Using JOIN, GROUP BY, and aggregate functions to count matches played by each team
SELECT TeamName, COUNT(*) as TotalMatches
FROM Plays
GROUP BY TeamName
ORDER BY TotalMatches DESC;

-- Using GROUP BY, ORDER BY, and aggregate functions to calculate average attendance per venue
SELECT Venue, AVG(Attendance) as AvgAttendance
FROM FootballMatch
WHERE Attendance IS NOT NULL
GROUP BY Venue
ORDER BY AvgAttendance DESC;

-- Using a single table to retrieve top scorer of each event
SELECT EventID, TopScorer
FROM Event
WHERE TopScorer IS NOT NULL;

-- Using GROUP BY, ORDER BY, and aggregate functions to sum goals scored in each round
SELECT Round, SUM(home_score + away_score) as TotalGoals
FROM FootballMatch
WHERE EventID = 2023
GROUP BY Round
ORDER BY TotalGoals DESC;

-- Using JOIN, sub-query, and aggregate functions to find matches with penalty kicks in a specific year
SELECT FM.*
FROM FootballMatch FM
JOIN Event E ON FM.EventID = E.EventID
WHERE (home_penalty IS NOT NULL OR away_penalty IS NOT NULL) AND E.EventYear = 2023;
