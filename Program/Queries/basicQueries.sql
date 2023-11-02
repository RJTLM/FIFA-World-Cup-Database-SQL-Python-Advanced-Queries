/* basicQueries.sql: MySQL file for basic queries*/

-- Q3. Part3 Level 1 Basic Queries:
-- basicQueries.sql: MySQL file for basic queries

-- Using string comparison to retrieve matches based on venue
-- SELECT * FROM FootballMatch WHERE Venue = 'Accor Stadium, Sydney';
-- Using string comparison to retrieve matches based on venue and filtering by EventID
SELECT * FROM FootballMatch WHERE Venue = 'Accor Stadium, Sydney' AND EventID = 9;

-- Using numeric data to retrieve matches based on attendance
SELECT * FROM FootballMatch WHERE Attendance > 50000;

-- Using date-time functions and BETWEEN to retrieve matches played in August 2023
SELECT * FROM FootballMatch WHERE MatchDate BETWEEN '2023-08-01' AND '2023-08-31';

-- Using string comparison and numeric data to retrieve specific matches
SELECT * FROM FootballMatch WHERE home_team = 'Spain' AND home_score > 2;

-- Using string comparison and checking for non-null values
SELECT * FROM FootballMatch WHERE Referee = 'Tori Penso' AND Notes IS NOT NULL;
