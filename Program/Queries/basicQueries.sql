/* basicQueries.sql: MySQL file for basic queries*/

-- Q3. Part3 Level 1 Basic Queries:
-- Find all matches played by a specific team
SELECT FM.* FROM FootballMatch FM
JOIN Plays P ON FM.MatchID = P.MatchID
WHERE P.TeamName IN ('Sweden');

-- Retrieve all matches with attendance greater than 50,000
SELECT * FROM FootballMatch WHERE Attendance > 50000;

-- Get details of matches played in August 2023
SELECT * FROM FootballMatch WHERE MatchDate BETWEEN '2023-08-01' AND '2023-08-31';

-- Find all matches where the home team scored more than 2 goals
SELECT * FROM FootballMatch WHERE home_score > 2;

-- Retrieve all matches refereed by a specific referee
SELECT * FROM FootballMatch WHERE RefereeName = 'Tori Penso';
