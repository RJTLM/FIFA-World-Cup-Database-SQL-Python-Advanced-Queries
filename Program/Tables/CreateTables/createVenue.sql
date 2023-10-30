/* createVenue.sql: MySQL file for creating the Venue table */

-- Q3. Part2a. Implementation:
-- Create Venue table
CREATE TABLE IF NOT EXISTS Venue (
  VenueName VARCHAR(255) PRIMARY KEY,
  Location VARCHAR(255) NOT NULL
);
