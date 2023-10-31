/* commands.sql: MySQL command file */

-- Q3. Part2a. Implementation:
-- Initialise Database and Tables

-- Create and Use fifa_womens_world_cup Database
source ./Program/Tables/CreateTables/createDatabase.sql;

-- Create tables that do not have foreign key dependencies (figured this out from trial and error)
source ./Program/Tables/CreateTables/createCountry.sql;
source ./Program/Tables/CreateTables/createCoach.sql;
source ./Program/Tables/CreateTables/createPlayer.sql;
source ./Program/Tables/CreateTables/createTeam.sql;
source ./Program/Tables/CreateTables/createVenue.sql;
source ./Program/Tables/CreateTables/createOfficialRole.sql;
source ./Program/Tables/CreateTables/createOfficial.sql;
source ./Program/Tables/CreateTables/createStage.sql;

-- Create tables that have foreign key dependencies
source ./Program/Tables/CreateTables/createEvent.sql;
source ./Program/Tables/CreateTables/createFootballMatch.sql;
source ./Program/Tables/CreateTables/createCard.sql;
source ./Program/Tables/CreateTables/createGoal.sql;
source ./Program/Tables/CreateTables/createSubstitution.sql;
source ./Program/Tables/CreateTables/createWinner.sql;

-- Create the relationship sets tables
source ./Program/Tables/CreateTables/createRelationshipSets.sql;