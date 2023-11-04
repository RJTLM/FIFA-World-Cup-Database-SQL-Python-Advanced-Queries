/* basicQueries.sql: MySQL file for basic queries*/

-- Q3. Part3 Level 1 Basic Queries:
-- Find all matches played by a specific team
/*SELECT FM.* FROM FootballMatch FM
JOIN Plays P ON FM.MatchID = P.MatchID
WHERE P.TeamName IN ('Sweden');*/
SELECT 
    FM.*,
    HomeTeam.TeamName AS HomeTeam,
    AwayTeam.TeamName AS AwayTeam
FROM 
    FootballMatch FM
JOIN 
    Plays AS HomePlays ON FM.MatchID = HomePlays.MatchID
JOIN 
    Team AS HomeTeam ON HomePlays.TeamName = HomeTeam.TeamName AND HomePlays.HomeOrAway = 'Home'
JOIN 
    Plays AS AwayPlays ON FM.MatchID = AwayPlays.MatchID
JOIN 
    Team AS AwayTeam ON AwayPlays.TeamName = AwayTeam.TeamName AND AwayPlays.HomeOrAway = 'Away'
WHERE 
    HomePlays.TeamName = 'Sweden' OR AwayPlays.TeamName = 'Sweden';


-- Retrieve all matches with attendance greater than 50,000
SELECT * FROM FootballMatch WHERE Attendance > 50000;

-- Get details of matches played in August 2023
SELECT * FROM FootballMatch WHERE MatchDate BETWEEN '2023-08-01' AND '2023-08-31';

-- Find all matches where the home team scored more than 2 goals
SELECT * FROM FootballMatch WHERE home_score > 2;

-- Retrieve all matches refereed by a specific referee
SELECT * FROM FootballMatch WHERE RefereeName = 'Tori Penso';
