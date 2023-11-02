/* advancedQueries.sql: MySQL file for advanced queries*/

-- Q3. Part3 Level 2 Advanced Queries:
-- Question 6: Which team has participated in the most matches?
SELECT TeamName, COUNT(MatchID) as Matches_Participated
FROM Plays
GROUP BY TeamName
ORDER BY Matches_Participated DESC
LIMIT 1;

-- Question 7: Which manager managed teams in the most number of different events?
SELECT ManagerName, COUNT(DISTINCT EventID) as Events_Managed
FROM Manages
JOIN FootballMatch ON Manages.MatchID = FootballMatch.MatchID
GROUP BY ManagerName
ORDER BY Events_Managed DESC
LIMIT 1;

-- Question 8: List all teams that have never won an event.
SELECT TeamName
FROM Team
WHERE TeamName NOT IN (SELECT Champion FROM Event);

-- Question 9: Which venue hosted the most matches?
SELECT Venue, COUNT(MatchID) as Matches_Hosted
FROM FootballMatch
GROUP BY Venue
ORDER BY Matches_Hosted DESC
LIMIT 1;

-- Question 10: Find the top scorer of the event with the highest average attendance.
SELECT TopScorer
FROM Event
WHERE EventAttendanceAvg = (SELECT MAX(EventAttendanceAvg) FROM Event);
