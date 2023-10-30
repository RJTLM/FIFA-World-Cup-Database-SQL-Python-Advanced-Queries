/* createOfficial.sql: MySQL file for creating the Official table */

-- Q3. Part2a. Implementation:
-- Create Official table
CREATE TABLE IF NOT EXISTS Official (
  OfficialName VARCHAR(255) PRIMARY KEY,
  Role VARCHAR(255) NOT NULL
);
