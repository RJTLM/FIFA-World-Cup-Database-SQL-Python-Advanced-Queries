/* createEvent.sql: MySQL file for creating the Event table */

-- Q3. Part2a. Implementation:
-- Create Event table with constraints
CREATE TABLE IF NOT EXISTS Event (
  EventID INT PRIMARY KEY,
  Year INT NOT NULL,
  HostCountry VARCHAR(255),
  Champion VARCHAR(255),
  RunnerUp VARCHAR(255),
  TopScorer VARCHAR(255),
  TotalAttendance INT NOT NULL,
  AvgAttendance INT,
  FOREIGN KEY (HostCountry) REFERENCES Country(CountryName) ON DELETE SET NULL
);
