-- Explain the index usage for MatchDate and Attendance
EXPLAIN SELECT * FROM FootballMatch USE INDEX (idx_date_attendance) WHERE YEAR(MatchDate) = 2023;
