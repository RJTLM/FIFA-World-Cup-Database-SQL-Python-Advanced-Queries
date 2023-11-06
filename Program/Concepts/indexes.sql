/* indexes.sql: MySQL file for indexes */

-- Index on TeamName in Plays Table to improve search performance
-- Reference: https://dev.mysql.com/doc/refman/8.0/en/create-index.html
CREATE INDEX idx_teamname ON Plays(TeamName);
