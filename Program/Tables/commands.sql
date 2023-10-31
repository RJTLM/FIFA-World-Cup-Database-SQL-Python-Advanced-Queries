-- Q3. Part2a. Implementation:
-- Initialise Database and Tables

-- Create and Use fifa_womens_world_cup Database
source ./CreateTables/createDatabase.sql;

-- Create Entity Sets Tables
source ./CreateTables/createCard.sql;
source ./CreateTables/createCoach.sql;
source ./CreateTables/createCountry.sql;
source ./CreateTables/createEvent.sql;
source ./CreateTables/createGoal.sql;
source ./CreateTables/createMatch.sql;
source ./CreateTables/createOfficial.sql;
source ./CreateTables/createOfficialRole.sql;
source ./CreateTables/createPlayer.sql;
source ./CreateTables/createStage.sql;
source ./CreateTables/createSubstitution.sql;
source ./CreateTables/createTeam.sql;
source ./CreateTables/createVenue.sql;
source ./CreateTables/createWinner.sql;

-- Create Relationship Sets Tables
source ./CreateTables/createRelationshipSets.sql;
