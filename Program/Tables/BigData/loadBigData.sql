LOAD DATA INFILE 'path/to/your/file/Program/bigDataCleaned.csv'
INTO TABLE BigData
FIELDS TERMINATED BY '\t' ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(MatchID, home_team, away_team, home_score, home_xg, home_penalty, away_score, away_xg, away_penalty,
home_manager, home_captain, away_manager, away_captain, Attendance, Venue, Officials, Round, @MatchDate,
Score, Referee, Notes, MatchHost, MatchYear, home_goal, away_goal, home_goal_long, away_goal_long,
home_own_goal, away_own_goal, home_penalty_goal, away_penalty_goal, home_penalty_miss_long, away_penalty_miss_long,
home_penalty_shootout_goal_long, away_penalty_shootout_goal_long, home_penalty_shootout_miss_long, away_penalty_shootout_miss_long,
home_red_card, away_red_card, home_yellow_red_card, away_yellow_red_card, home_yellow_card_long, away_yellow_card_long,
home_substitute_in_long, away_substitute_in_long, EventID, EventYear, EventHost, NoTeams, Champion, RunnerUp,
TopScorer, EventAttendance, EventAttendanceAvg, NoMatches)
SET MatchDate = STR_TO_DATE(@MatchDate, '%Y/%m/%d');
