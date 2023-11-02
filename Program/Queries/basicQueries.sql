/* basicQueries.sql: MySQL file for basic queries*/

-- Q3. Part3 Level 1 Basic Queries:
-- Question 1: Who won the 2023 FIFA Women's World Cup?
SELECT Champion 
FROM Event 
WHERE EventYear = 2023 AND EventHost = 'FIFA Women''s World Cup';

-- Question 2: What dates were the 2023 semi-finals played on and what were the match details?
SELECT MatchDate, home_team.TeamName AS home_team, away_team.TeamName AS away_team, home_score, away_score
FROM FootballMatch
JOIN Team AS home_team ON FootballMatch.home_team = home_team.TeamID
JOIN Team AS away_team ON FootballMatch.away_team = away_team.TeamID
WHERE Round = 'Semi-finals' AND EventID = (SELECT EventID FROM Event WHERE EventYear = 2023)
ORDER BY MatchDate;

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
