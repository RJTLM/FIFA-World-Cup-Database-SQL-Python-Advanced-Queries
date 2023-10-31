-- Undo Data Insertions for fifa_womens_world_cup Database
USE fifa_womens_world_cup_21171466;

-- Delete Data from PlayedAt Table
DELETE FROM PlayedAt WHERE MatchID = 348 AND VenueName = 'Accor Stadium, Sydney';

-- Delete Data from ParticipatesIn Table
DELETE FROM ParticipatesIn WHERE EventID = 9;

-- Delete Data from Hosts Table
DELETE FROM Hosts WHERE EventID = 9;

-- Delete Data from ConsistsOf Table
DELETE FROM ConsistsOf WHERE StageRound = 'Final' AND MatchID = 348;

-- Delete Data from Stage Table
DELETE FROM Stage WHERE Round = 'Final';

-- Delete Data from OfficiatedBy Table
DELETE FROM OfficiatedBy WHERE MatchID = 348;

-- Delete Data from Official Table
DELETE FROM Official WHERE OfficialName IN ('Tori Penso', 'Brooke Mayo', 'Kathryn Nesbitt', 'Yoshimi Yamashita', 'Tatiana Guzman');

-- Delete Data from Substitution Table
DELETE FROM Substitution WHERE MatchID = 348;

-- Delete Data from Card Table
-- Note: No card data was inserted in the provided script

-- Delete Data from Goal Table
DELETE FROM Goal WHERE GoalID = 1;

-- Delete Data from FootballMatch Table
DELETE FROM FootballMatch WHERE MatchID = 348;

-- Update Team Table to Remove Managers and Captains
UPDATE Team SET Manager = NULL, Captain = NULL WHERE TeamName IN ('Spain', 'England');

-- Delete Data from Player Table
DELETE FROM Player WHERE PlayerName IN ('Olga Carmona', 'Millie Bright', 'Mariona Caldentey', 'Jennifer Hermoso', 'Salma Paralluelo', 'Lauren Hemp', 'Oihane Hernandez', 'Alba Redondo', 'Laia Codina', 'Ivana Andres', 'Alexia Putellas', 'Alessia Russo', 'Rachel Daly', 'Chloe Kelly', 'Ella Toone', 'Bethany England', 'Lauren James');

-- Delete Data from Team Table
DELETE FROM Team WHERE TeamName IN ('Spain', 'England');

-- Delete Data from Event Table
DELETE FROM Event WHERE EventID = 9;

-- Delete Data from Venue Table
DELETE FROM Venue WHERE VenueName = 'Accor Stadium, Sydney';

-- Delete Data from Country Table
DELETE FROM Country WHERE CountryName IN ('Australia', 'New Zealand', 'Spain', 'England');

-- Note to self: Ensure to check if there are any other dependencies or constraints that need to be addressed before running this script.
