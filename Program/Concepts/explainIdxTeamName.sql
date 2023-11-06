-- Explain the index usage for TeamName
EXPLAIN SELECT * FROM Plays USE INDEX (idx_teamname) WHERE TeamName = 'USA';
