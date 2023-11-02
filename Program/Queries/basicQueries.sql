/* basicQueries.sql: MySQL file for basic queries*/

-- Q3. Part3 Level 1 Basic Queries:
-- Question 1: How many teams participated in events hosted in 2023?
SELECT COUNT(DISTINCT TeamName) 
FROM Plays 
JOIN FootballMatch ON Plays.MatchID = FootballMatch.MatchID
JOIN Event ON FootballMatch.EventID = Event.EventID
WHERE Event.EventYear = 2023;

-- Question 2: What is the total attendance for events held in 2023?
SELECT SUM(EventAttendance) 
FROM Event
WHERE EventYear = 2023;

-- Question 3: Which referee officiated the most matches?
SELECT RefereeName, COUNT(MatchID) as Matches_Officiated
FROM FootballMatch
WHERE RefereeName IS NOT NULL
GROUP BY RefereeName
ORDER BY Matches_Officiated DESC
LIMIT 1;

-- Question 4: What is the average number of matches per event?
SELECT AVG(NoMatches) 
FROM Event;

-- Question 5: List all players who are captains.
SELECT PlayerName
FROM Player
WHERE isCaptain = TRUE;
