/* createWinner.sql: MySQL file for creating the Winner table */

-- Q3. Part2a. Implementation:
-- Create Winner table
Table: Winner(MatchID)
Primary Key: MatchID
Foreign Key: MatchID references Match(MatchID)
Referential Integrity Constraints: ON DELETE CASCADE for MatchID
