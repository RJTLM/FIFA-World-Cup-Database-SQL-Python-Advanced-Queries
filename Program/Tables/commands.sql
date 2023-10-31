/* commands.sql: MySQL command file */

-- Q3. Part2a. Implementation:
-- Initialise Database and Tables

-- Create and Use fifa_womens_world_cup Database
source ./Program/Tables/CreateTables/createDatabase.sql;

-- Create Entity Sets Tables
source ./Program/Tables/CreateTables/createCard.sql;
source ./Program/Tables/CreateTables/createCoach.sql;
source ./Program/Tables/CreateTables/createCountry.sql;
source ./Program/Tables/CreateTables/createEvent.sql;
source ./Program/Tables/CreateTables/createGoal.sql;
source ./Program/Tables/CreateTables/createFootballMatch.sql;
source ./Program/Tables/CreateTables/createOfficial.sql;
source ./Program/Tables/CreateTables/createOfficialRole.sql;
source ./Program/Tables/CreateTables/createPlayer.sql;
source ./Program/Tables/CreateTables/createStage.sql;
source ./Program/Tables/CreateTables/createSubstitution.sql;
source ./Program/Tables/CreateTables/createTeam.sql;
source ./Program/Tables/CreateTables/createVenue.sql;
source ./Program/Tables/CreateTables/createWinner.sql;

-- Create Relationship Sets Tables
source ./Program/Tables/CreateTables/createRelationshipSets.sql;
