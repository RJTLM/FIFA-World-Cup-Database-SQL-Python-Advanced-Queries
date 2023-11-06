/* indexes.sql: MySQL file for indexes */

-- Indexes
-- Index on TeamName in Plays Table to improve search performance
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-index.html
CREATE INDEX idx_teamname ON Plays(TeamName);

-- Index on MatchDate and Attendance in FootballMatch Table to improve query performance
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-index.html
CREATE INDEX idx_date_attendance ON FootballMatch(MatchDate, Attendance);

-- To demonstrate improved performance:
-- Query without index: EXPLAIN SELECT * FROM Plays WHERE TeamName = 'USA';
-- Query with index: EXPLAIN SELECT * FROM Plays USE INDEX (idx_teamname) WHERE TeamName = 'USA';
-- Query using the index should have a lower row scan count, indicating a more efficient query execution.
-- Reference for EXPLAIN: https://dev.mysql.com/doc/refman/8.0/en/explain.html
