-- Load Data into fifa_womens_world_cup Database
USE fifa_womens_world_cup_21171466;

-- Insert Data into Country Table
INSERT INTO Country (CountryName) VALUES ('Australia'), ('New Zealand'), ('Spain'), ('England');

-- Insert Data into Venue Table
INSERT INTO Venue (VenueName, Location) VALUES ('Accor Stadium, Sydney', 'Sydney');

-- Insert Data into Event Table
INSERT INTO Event (EventID, Year, HostCountry, Champion, RunnerUp, TopScorer, TotalAttendance, AvgAttendance) VALUES (9, 2023, 'Australia', 'Spain', 'England', 'Hinata Miyazawa', 1976274, 30879);

-- Insert Data into Team Table
INSERT INTO Team (TeamName) VALUES ('Spain'), ('England');

-- Insert Data into Player Table
INSERT INTO Player (PlayerName, TeamName) VALUES ('Olga Carmona', 'Spain'), ('Millie Bright', 'England'), ('Mariona Caldentey', 'Spain'), ('Jennifer Hermoso', 'Spain'), ('Salma Paralluelo', 'Spain'), ('Lauren Hemp', 'England'), ('Oihane Hernandez', 'Spain'), ('Alba Redondo', 'Spain'), ('Laia Codina', 'Spain'), ('Ivana Andres', 'Spain'), ('Alexia Putellas', 'Spain'), ('Alessia Russo', 'England'), ('Rachel Daly', 'England'), ('Chloe Kelly', 'England'), ('Ella Toone', 'England'), ('Bethany England', 'England'), ('Lauren James', 'England');

-- Insert Data into Coach Table
INSERT INTO Coach (CoachName) VALUES ('Jorge Vilda'), ('Sarina Wiegman');

-- Update Team Table with Managers and Captains
UPDATE Team SET Manager = 'Jorge Vilda', Captain = 'Olga Carmona' WHERE TeamName = 'Spain';
UPDATE Team SET Manager = 'Sarina Wiegman', Captain = 'Millie Bright' WHERE TeamName = 'England';

-- Insert Data into Match Table
INSERT INTO Match (MatchID, Date, HomeTeam, AwayTeam, HomeScore, AwayScore, Attendance, VenueName, Round, Notes) VALUES (348, '2023-08-20', 'Spain', 'England', 1, 0, 75784, 'Accor Stadium, Sydney', 'Final', NULL);

-- Insert Data into Goal Table
INSERT INTO Goal (GoalID, MatchID, ScoringTeam, Scorer, Assist, Time, Type) VALUES (1, 348, 'Spain', 'Olga Carmona', 'Mariona Caldentey', 29, 'Regular');

-- Insert Data into Card Table
-- Note: No card data provided in the sample row

-- Insert Data into Substitution Table
INSERT INTO Substitution (SubstitutionID, MatchID, Time, PlayerOut, PlayerIn, TeamName) VALUES (1, 348, 60, 'Alba Redondo', 'Oihane Hernandez', 'Spain'), (2, 348, 73, 'Laia Codina', 'Ivana Andres', 'Spain'), (3, 348, 90, 'Mariona Caldentey', 'Alexia Putellas', 'Spain'), (4, 348, 46, 'Alessia Russo', 'Lauren James', 'England'), (5, 348, 46, 'Rachel Daly', 'Chloe Kelly', 'England'), (6, 348, 87, 'Ella Toone', 'Bethany England', 'England');

-- Insert Data into Official Table
INSERT INTO Official (OfficialName, Role) VALUES ('Tori Penso', 'Referee'), ('Brooke Mayo', 'Assistant Referee 1'), ('Kathryn Nesbitt', 'Assistant Referee 2'), ('Yoshimi Yamashita', 'Fourth Official'), ('Tatiana Guzman', 'VAR');

-- Insert Data into OfficiatedBy Table
INSERT INTO OfficiatedBy (MatchID, OfficialName) VALUES (348, 'Tori Penso'), (348, 'Brooke Mayo'), (348, 'Kathryn Nesbitt'), (348, 'Yoshimi Yamashita'), (348, 'Tatiana Guzman');

-- Insert Data into Stage Table
INSERT INTO Stage (Round) VALUES ('Final');

-- Insert Data into ConsistsOf Table
INSERT INTO ConsistsOf (StageRound, MatchID) VALUES ('Final', 348);

-- Insert Data into Hosts Table
INSERT INTO Hosts (CountryName, EventID) VALUES ('Australia', 9), ('New Zealand', 9);

-- Insert Data into ParticipatesIn Table
-- Note: This requires Player and Event data to be present
INSERT INTO ParticipatesIn (PlayerName, EventID) VALUES ('Olga Carmona', 9), ('Millie Bright', 9), ('Mariona Caldentey', 9), ('Jennifer Hermoso', 9), ('Salma Paralluelo', 9), ('Lauren Hemp', 9), ('Oihane Hernandez', 9), ('Alba Redondo', 9), ('Laia Codina', 9), ('Ivana Andres', 9), ('Alexia Putellas', 9), ('Alessia Russo', 9), ('Rachel Daly', 9), ('Chloe Kelly', 9), ('Ella Toone', 9), ('Bethany England', 9), ('Lauren James', 9);

-- Insert Data into PlayedAt Table
INSERT INTO PlayedAt (MatchID, VenueName) VALUES (348, 'Accor Stadium, Sydney');
