/* deleteDatabase.sql: MySQL file for database creation*/

-- Created this for better UX when testing, refactoring and debugging so I didn't need to exit program

-- Delete tables if they exist
DROP TABLE IF EXISTS BigData, Event, FootballMatch, LittleData, Manager, Manages, Player, Plays, Referee, Team;

-- Delete the database
DROP DATABASE IF EXISTS fifa_womens_world_cup_21171466;
