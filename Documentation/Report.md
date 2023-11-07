# **Database Design and Implementation Report**

## Cover Page

### Final Assessment: Database System for FIFA Women's World Cup
#### Student Name: Ryan Mackintosh
#### Student ID: 21171466
#### Lab Group: Thursday 8am

## Table of Contents

- [Introduction](#introduction)
- [Design of the Database](#design-of-the-database)
  - [Entity Selection](#entity-selection)
  - [ER Diagram](#er-diagram)
  - [Relational Schema](#relational-schema)
  - [Data Description](#data-description)
  - [Assumptions](#assumptions)
- [Implementation of the Database and Adding Sample Data](#implementation-of-the-database-and-adding-sample-data)
  - [Database Implementation](#database-implementation)
  - [Sample Data and Insertion](#sample-data-and-insertion)
- [Use of the Database](#use-of-the-database)
  - [Queries](#queries)
  - [Advanced Features](#advanced-features)
  - [Database Connectivity and Python Implementation](#database-connectivity-and-python-implementation)
- [Discussion](#discussion)
- [References](#references)

## Introduction

In this report, I present an overview of the work I have done to design, implement, and query a relational database system tailored for the FIFA Women's World Cup scenario. The entire program operates within a Python environment, specifically for a Linux command-line interface (CLI), ensuring seamless execution and interaction without the need for direct MySQL database access.

Throughout this project, I have followed the step-by-step process taught in the lecture slides to design an entity-relationship model, implement a relational schema, and populate a database with sample data. Furthermore, I created and executed a suite of SQL queries, using advanced features such as stored procedures and views to enhance the database's functionality. The culmination of these efforts (along with my painful perfectionism) is a system that meets the specified requirements and also demonstrates the practical application of modern database concepts.

I have documented the entire process, reflecting on the design and implementation decisions, identifying challenges, and suggesting improvements. This documentation serves as a testament to the numerous hours spent testing, refactoring, and debugging to ensure the delivery of a high-quality database system.

If you are interested in a more intricate view of the development of my project, you are welcome to review my private GitHub repository (happy to give access just don't want to compromise academic integrity), which contains well over 200 commits that highlight the pain I experienced testing and refactoring, refactoring and testing, and then some more (and also the evolution of this assignment). The repository is a testament to the dedication and rigorous attention to detail that has been the hallmark of this project.

[GitHub Repository: RJTLM/DSFinalAssignment](https://github.com/RJTLM/DSFinalAssignment)

By doing this assignment I have been able to apply theoretical knowledge learned in class to a real-world context, and the following sections will detail the processes and methodologies used to achieve (and not quite) the objectives set forth.


## Design of the Database

### Entity Selection

In designing the database for the FIFA Women's World Cup, careful consideration was given to the selection of entities, their relationships, and the data types of their attributes. The goal was to create a robust and scalable model that accurately reflects the complexities of the tournament while remaining intuitive and efficient for querying and data manipulation.

#### Entities and Attributes

The primary entities identified for this database are `Match`, `Team`, `Player`, `Event`, `Manager`, and `Referee`. These entities encompass the core components of the tournament and are described as follows:

- **Match**: Represents individual games played within the tournament. Attributes include unique identifiers, scores, penalties, attendance, venue, and related event information. The `MatchID` serves as the primary key, ensuring each match is uniquely identifiable.
  
- **Team**: Captures the teams participating in the World Cup. The `TeamName` is the primary key and is used to link players and matches to teams.
  
- **Player**: Details the players, including whether they are a team captain. The `PlayerName` is the primary key, and the `isCaptain` attribute is a boolean indicating captaincy.
  
- **Event**: Encapsulates the overall tournament event, with attributes detailing the year, host, number of teams, and outcomes such as the champion and top scorer. The `EventID` is the primary key.
  
- **Manager**: Contains information on team managers. The `ManagerName` is the primary key.
  
- **Referee**: Contains information on match referees. The `RefereeName` is the primary key.

#### Relationships

The relationships between entities are critical to the relational schema and are defined as follows:

- **Plays**: A many-to-many relationship between `Match` and `Team`, indicating which teams play in which matches. Attributes include `MatchID`, `TeamName`, and `HomeAway` to indicate whether the team is playing at home or away.
  
- **Manages**: A many-to-many relationship between `Match` and `Manager`, indicating which manager manages a team in a particular match.
  
- **PlaysFor**: A many-to-many relationship between `Player` and `Team`, indicating which players play for which teams.
  
- **Is Played In**: A one-to-many relationship between `Match` and `Event`, linking matches to the event they are part of.

#### Data Types

Data types were chosen to best represent the nature of the data while optimizing for storage and performance:

- **Integer (INT)**: Used for numerical values that do not require decimals, such as scores, attendance, and identifiers.
  
- **Varchar**: Used for string attributes that require a variable length, such as names and textual descriptions.
  
- **Boolean**: Used for true/false values, specifically for the `isCaptain` attribute in the `Player` entity.
  
- **Date**: Used for date attributes to track when matches are played.
  
- **Enum**: Used for attributes with a controlled list of values, such as the `HomeAway` attribute in the `Plays` relationship.

#### Cardinality Constraints

Cardinality constraints define the nature of the relationships in terms of quantity:

- **One-to-Many**: Used for relationships where one instance of an entity relates to many instances of another, such as a single event having multiple matches.
  
- **Many-to-Many**: Used for relationships where many instances of an entity relate to many instances of another, such as players playing for teams and teams playing in matches.

#### Participation Constraints

Participation constraints specify the minimum and maximum number of entity instances that can participate in a relationship:

- **Mandatory Participation**: Indicates that an entity must participate in the relationship, such as every match must be associated with an event.
  
- **Optional Participation**: Indicates that an entity's participation in the relationship is not required, such as a player not needing to be a captain.

The entity selection and relationship mapping were done with the intention of creating a database that is not only reflective of the real-world domain but also optimized for query performance and data integrity. The chosen data types and constraints ensure that the database is normalized, reducing redundancy and improving data consistency.

#### Entity Sets, Relationship Sets, and Cardinality Constraints

**Entity Set**
| Entity Set   | Key         | Other Attributes                                                                                      | Relationship Set | Between Entity Sets | Attributes | Relationship Set Cardinality | Participation / Other Constraints                      |
|--------------|-------------|-------------------------------------------------------------------------------------------------------|------------------|---------------------|------------|-----------------------------|--------------------------------------------------------|
| Match        | MatchID     | home_score, away_score, home_penalty, away_penalty, Attendance, Venue, Round, MatchDate, Notes, MatchHost | Is Played In     | Match-Event         | EventID    | Many-One                    | Each Match is associated with one Event; An Event can have multiple Matches |
| Team         | TeamName    |                                                                                                       | Plays            | Match-Team          | MatchID, HomeAway | Many-Many                | A Team can play in many Matches; A Match involves two Teams |
| Player       | PlayerName  | isCaptain                                                                                             | PlaysFor                 | Player-Team                    | PlayerName, TeamName           | Many-Many                             | Many Players can play for a Team; A Team has many Players                                                          |
| Event        | EventID     | EventYear, EventHost, NoTeams, Champion, RunnerUp, TopScorer, EventAttendance, EventAttendanceAvg, NoMatches | Is Played In     | Match-Event         | MatchID    | Many-One                    | Each Match is associated with one Event; An Event can have multiple Matches |
| Manager      | ManagerName |                                                                                                       | Manages          | Match-Manager       | MatchID    | Many-Many                    | A Manager can manage in many Matches; A Match can have multiple Managers |
| Referee      | RefereeName |                                                                                                       | Officiates       | Match-Referee       | MatchID    | Many-One                    | A Referee can officiate many Matches; A Match is officiated by one Referee |

**Relationship Set**
| Relationship Set | Between Entity Sets | Attributes | Relationship Set Cardinality | Participation / Other Constraints |
|------------------|---------------------|------------|-----------------------------|--------------------------------------------------------|
| Plays            | Match-Team          | MatchID, TeamName, HomeAway | Many-Many                | A Team can play in many Matches; A Match involves two Teams |
| Manages          | Match-Manager       | MatchID, ManagerName | Many-Many                    | A Manager can manage in many Matches; A Match can have multiple Managers |
| Officiates       | Match-Referee       | MatchID, RefereeName | Many-One                    | A Referee can officiate many Matches; A Match is officiated by one Referee |
| Is Played In     | Match-Event         | MatchID, EventID | Many-One                    | Each Match is associated with one Event; An Event can have multiple Matches |

### ER Diagram

![ER Diagram](../ERModelling/ERDiagram.png)

### Relational Schema

#### Entity Sets

##### FootballMatch
```
FootballMatch(MatchID, home_score, away_score, home_penalty, away_penalty, Attendance, Venue, Round, MatchDate, Notes, MatchHost, EventID, RefereeName)
FK EventID REF Event(EventID)
FK RefereeName REF Referee(RefereeName)
```

##### Team
```
Team(TeamName)
```

##### Player
```
Player(PlayerName, isCaptain)
```

##### Manager
```
Manager(ManagerName)
```

##### Referee
```
Referee(RefereeName)
```

##### Event
```
Event(EventID, EventYear, EventHost, NoTeams, Champion, RunnerUp, TopScorer, EventAttendance, EventAttendanceAvg, NoMatches)
```

#### Relationship Sets (Represented as Tables for Many-to-Many Relationships)

##### Plays
```
Plays(MatchID, TeamName, HomeAway)
FK MatchID REF FootballMatch(MatchID)
FK TeamName REF Team(TeamName)
```

##### Manages
```
Manages(MatchID, ManagerName)
FK MatchID REF FootballMatch(MatchID)
FK ManagerName REF Manager(ManagerName)
```

##### PlaysFor
```
PlaysFor(PlayerName, TeamName)
FK PlayerName REF Player(PlayerName)
FK TeamName REF Team(TeamName)
```

### Data Description

#### FootballMatch

| Attribute    | Data Type    | Constraints | Description                               | Business Rules                                         |
|--------------|--------------|-------------|-------------------------------------------|--------------------------------------------------------|
| MatchID      | INT          | PK, NOT NULL, UNIQUE | Unique identifier for each match       | Must be unique                                         |
| home_score   | INT          |             | Score of the home team                    | Can be null if match hasn't been played yet            |
| away_score   | INT          |             | Score of the away team                    | Can be null if match hasn't been played yet            |
| home_penalty | INT          |             | Penalty score of the home team            | Can be null if match hasn't gone to penalties          |
| away_penalty | INT          |             | Penalty score of the away team            | Can be null if match hasn't gone to penalties          |
| Attendance   | INT          |             | Number of attendees at the match          | Can be null if match hasn't been played yet            |
| Venue        | VARCHAR(255) |             | Location where the match is played        | Can be null if venue is not decided yet                |
| Round        | VARCHAR(50)  |             | Stage of the competition                  | Can be null if not applicable                          |
| MatchDate    | DATE         |             | Date when the match is played             | Can be null if date is not decided yet                 |
| Notes        | TEXT         |             | Additional notes about the match          | Can be null                                            |
| MatchHost    | VARCHAR(255) |             | Host country or city of the match         | Can be null if not applicable                          |
| EventID      | INT          | FK referencing Event(EventID), ON DELETE CASCADE, ON UPDATE CASCADE | ID of the event the match is part of | Must correspond to an existing EventID                |
| RefereeName  | VARCHAR(255) | FK referencing Referee(RefereeName), ON DELETE SET NULL, ON UPDATE CASCADE | Name of the referee officiating the match | Can be null if referee is not decided yet, must correspond to an existing RefereeName |

#### Team

| Attribute | Data Type    | Constraints | Description               | Business Rules |
|-----------|--------------|-------------|---------------------------|----------------|
| TeamName  | VARCHAR(255) | PK, NOT NULL, UNIQUE | Name of the football team | Must be unique |

#### Player

| Attribute  | Data Type | Constraints | Description               | Business Rules                         |
|------------|-----------|-------------|---------------------------|----------------------------------------|
| PlayerName | VARCHAR(255) | PK, NOT NULL, UNIQUE | Name of the player      | Must be unique                         |
| isCaptain  | BOOLEAN   | DEFAULT FALSE | Indicates if player is captain | Only 1 captain per team per event |

#### Event

| Attribute         | Data Type    | Constraints | Description                           | Business Rules |
|-------------------|--------------|-------------|---------------------------------------|----------------|
| EventID           | INT          | PK, NOT NULL, UNIQUE | Unique identifier for each event   | Must be unique |
| EventYear         | YEAR         |             | Year when the event took place        | Can be null if event is planned for future |
| EventHost         | VARCHAR(255) |             | Host country or city of the event     | Can be null if not applicable |
| NoTeams           | INT          |             | Number of teams participating         | Can be null if not decided yet |
| Champion          | VARCHAR(255) |             | Winning team of the event             | Can be null if event hasn't concluded yet |
| RunnerUp          | VARCHAR(255) |             | Runner-up team of the event           | Can be null if event hasn't concluded yet |
| TopScorer         | VARCHAR(255) |             | Top scorer of the event               | Can be null if event hasn't concluded yet |
| EventAttendance   | INT          |             | Total attendance throughout the event | Can be null if event hasn't concluded yet |
| EventAttendanceAvg| FLOAT        |             | Average attendance per match          | Can be null if event hasn't concluded yet |
| NoMatches         | INT          |             | Number of matches in the event        | Can be null if not decided yet |

#### Manager

| Attribute   | Data Type    | Constraints | Description             | Business Rules |
|-------------|--------------|-------------|-------------------------|----------------|
| ManagerName | VARCHAR(255) | PK, NOT NULL, UNIQUE | Name of the manager | Must be unique |

#### Referee

| Attribute   | Data Type    | Constraints | Description             | Business Rules |
|-------------|--------------|-------------|-------------------------|----------------|
| RefereeName | VARCHAR(255) | PK, NOT NULL, UNIQUE | Name of the referee | Must be unique |

#### Plays (Many-to-Many Relationship)

| Attribute | Data Type    | Constraints | Description             | Business Rules |
|-----------|--------------|-------------|-------------------------|----------------|
| MatchID   | INT          | FK referencing FootballMatch(MatchID), ON DELETE CASCADE, ON UPDATE CASCADE | ID of the match | Must correspond to an existing MatchID |
| TeamName  | VARCHAR(255) | FK referencing Team(TeamName), ON DELETE CASCADE, ON UPDATE CASCADE | Name of the team | Must correspond to an existing TeamName |
| HomeAway  | ENUM('Home', 'Away') | NOT NULL | Indicates if the team is playing at home or away | Must be 'Home' or 'Away' |

#### Manages (Many-to-Many Relationship)

| Attribute   | Data Type    | Constraints | Description             | Business Rules |
|-------------|--------------|-------------|-------------------------|----------------|
| MatchID     | INT          | FK referencing FootballMatch(MatchID), ON DELETE CASCADE, ON UPDATE CASCADE | ID of the match | Must correspond to an existing MatchID |
| ManagerName | VARCHAR(255) | FK referencing Manager(ManagerName), ON DELETE CASCADE, ON UPDATE CASCADE | Name of the manager | Must correspond to an existing ManagerName |

#### PlaysFor (Many-to-Many Relationship)

| Attribute   | Data Type    | Constraints | Description             | Business Rules |
|-------------|--------------|-------------|-------------------------|----------------|
| PlayerName     | VARCHAR(255)          | FK referencing Player(PlayerName), ON DELETE CASCADE, ON UPDATE CASCADE | Name of the player | Must correspond to an existing PlayerName |
| TeamName | VARCHAR(255) | FK referencing Team(TeamName), ON DELETE CASCADE, ON UPDATE CASCADE | Name of the team | Must correspond to an existing TeamName |

### Third Normal Form

Normalization is a systematic approach of decomposing tables to eliminate data redundancy and undesirable characteristics like Insertion, Update, and Deletion Anomalies. It's a multi-step process that puts data into tabular form by removing duplicated data from the relation tables.

#### First Normal Form (1NF)
For a table to be in 1NF, it must have:
1. No repeating groups or arrays.
2. All values must be atomic (indivisible).

My Schema:
- Each attribute has atomic values (no multi-valued attributes).
- There are no repeating groups; for example, `Plays` and `Manages` are separate tables, which indicates that many-to-many relationships are handled properly.

#### Second Normal Form (2NF)
For a table to be in 2NF, it must be in 1NF, and:
1. All non-key attributes must be fully functionally dependent on the primary key.

2NF only applies to tables with composite primary keys (primary keys consisting of more than one attribute):
- `Plays` and `Manages` have composite keys (`MatchID` and `TeamName` for `Plays`; `MatchID` and `ManagerName` for `Manages`). In these tables, all non-key attributes are fully dependent on the full set of key attributes.

#### Third Normal Form (3NF)
For a table to be in 3NF, it must be in 2NF, and:
1. It has no transitive dependencies; that is, no non-key attribute depends on another non-key attribute.

My Schema:
- `FootballMatch` has foreign keys (`EventID`, `RefereeName`) that reference primary keys in other tables (`Event`, `Referee`). There are no attributes in `FootballMatch` that are non-key and depend on other non-key attributes.
- `Event` has attributes like `Champion`, `RunnerUp`, and `TopScorer`, which are dependent on `EventID` and not on any other non-key attribute.
- `Plays` and `Manages` do not have non-key attributes that depend on other non-key attributes.

All tables are in 3NF because each table has a primary key that uniquely identifies its rows, and there are no attributes that are dependent on non-key attributes, which eliminates transitive dependencies.

### Assumptions

1. **Standardized Data Formats**: All data entered into the database follows standardized formats to ensure consistency and reliability in data handling and queries.
2. **Data Completeness**: The data for all matches, teams, and players is assumed to be complete and available for entry into the database.
4. **Unique Identifiers**: Each player, team, match, and event has a unique identifier that ensures there are no duplicates within the database.
5. **Predefined Host Locations**: The host locations for matches are predefined and known prior to the tournament's commencement.
7. **Single Role Per Person**: Individuals are assumed to have a single role within the database context, i.e., a person cannot be both a player and a referee.
8. **Based on Historical Data**: The database design and assumptions are based on historical data and trends from previous tournaments.
9. **Stable Database Schema**: The database schema is assumed to be stable with no significant changes expected after the initial design.
10. **Data Accuracy**: The data provided for input into the database is assumed to be accurate and verified.
11. **Event Scheduling**: All events are scheduled in advance, and the database is updated accordingly to reflect any changes.
13. **Team Participation**: Each team is assumed to participate in the entire duration of the tournament unless disqualified or withdrawn.
14. **Database Security**: Database security is a requirement, thus access control via username and password is essential to protect sensitive data.
15. **Tournament Data Focus**: The database is primarily focused on capturing and providing insights into tournament-level data, such as match outcomes, team progress, and crowd attendance. It is not designed to delve into detailed internal match statistics beyond standard information such as the winner, loser, scores, and basic event occurrences.

These assumptions are integral to the design and implementation of the database, providing a framework within which the database operates and ensuring that users have a clear understanding of its scope and limitations.

## Implementation of the Database and Adding Sample Data

### Database Implementation

My journey to create a Python program for the FIFA Women's World Cup database was driven by a goal to exceed the project's outlined requirements. The vision was to engineer a system that would facilitate every operation detailed in the assignment brief through the command-line interface (CLI), thus eliminating the need for direct MySQL database interaction.

The initial challenge was cleaning the provided CSV files. The global diversity of the dataset introduced player names with non-ASCII characters, which necessitated a cleanup. To resolve this, I created `asciiConversion.py`, a script that cleaned and converted non-ASCII characters to their ASCII counterparts, ensuring compatibility throughout the system.

Following this, I built `dataViewer.py`. This utility allowed for the inspection of CSV files directly through the CLI, bypassing the need for spreadsheet applications (Excel, etc.).

The `extractData.py` script was next in line, designed to extract only the essential columns required for database insertion. This file allowed me to extract the data I wanted (to minimise potential issues later on).

I then created `splitColumn.py` with the intent to utilize the entirety of the CSV data. However, the realization that this approach was beyond the project's scope (even for me, (ha ha I'm so funny)) led to a reevaluation. The script, while functional, represented an overly complex solution for a simpler task.

Central to the user experience was `menu.py`, a script that functioned as the gateway for the suite of tools. It provided a user-friendly menu system, allowing for seamless navigation and operation of the various functionalities, all from within the CLI.

With the groundwork laid by these tools, I focused on the database implementation. `mySQLConnector.py` served as the entry point, facilitating database connection upon user authentication (hidden password too).

The database's construction was a phased operation, involving a series of scripts and SQL files. `createTables.py` laid the foundation, while `createDatabase.sql`, `useDatabase.sql`, `createTablesWithoutFKDep.sql`, `createTablesWithFKDep.sql`, and `createRelationshipSets.sql` each contributed to the structural and relational development of the database. It is worth noting that the tables without any dependencies were created first, then tables with dependencies and then relationship (many-to-many) tables.

Finally, `deleteDatabase.sql` provided a means to reset the database, a crucial feature for testing and iterative refinement, ensuring the robustness of the final product.

In short, every script and SQL file played its part, coming together to build a system that is user friendly, and simpler than directly accessing MySQL to manage databases.

### Sample Data and Insertion

This phase of the project was, without a doubt, the most challenging and time-consuming. I found myself diving deep into the intricacies of data insertion, a task that proved to be more complex than anticipated. The lack of clear guidance on how to insert data from CSV files directly into MySQL tables led me down a path of extensive research and experimentation.

Initially, I attempted to create a comprehensive table that could hold all CSV data by using `createBigDataTable.sql` and `insertBigData.sql`. However, this approach hit a dead end when I realized it wasn't feasible. It was during this period of trial and error that I decided to narrow the scope of my database to focus solely on tournament data, as the player information provided in the CSV files was causing numerous issues due to its format.

After much deliberation and testing various strategies, I discovered that Python could in fact be used to insert data directly into each table, bypassing the need for intermediary SQL scripts. This led to the the final version of `insertData.py`, a script that became the anchor for data insertion.

The `insertData.py` script begins by clearing any existing data in the tables to ensure a clean slate for insertion. The script then proceeds to insert data into various tables such as Team, Player, Manager, Referee, Event, FootballMatch, Plays, and Manages. It uses a combination of `INSERT` and `INSERT IGNORE` statements to add new records while avoiding duplicates, especially for entries like team names, player names, and manager names that could potentially repeat.

For instance, when inserting into the Event table, the script reads from `littleDataCleaned.csv`, iterating over each row and using a prepared statement to insert the data. Similarly, for the FootballMatch and related tables, it utilizes `bigDataCleaned1.csv`. The script ensures that all related data, such as match details, team participation, and management roles, are correctly associated with each other in the database.

The script handles exceptions gracefully, reporting any errors encountered during the insertion process and rolling back changes if necessary to maintain database integrity. Upon successful insertion, it commits the changes to the database and confirms the completion of the operation.

In summary, `insertData.py` is a robust and efficient solution for populating the database with sample data. It encapsulates the complexity of data insertion into a streamlined process, allowing for accurate and reliable database population directly through Python.

## Use of the Database

### Queries

_Design and implementation of queries with explanations and sample outputs._

### Advanced Features

_Description of advanced features implemented, their use, and evidence of outputs._

### Database Connectivity and Python Implementation

_Description of the database connectivity implementation with evidence._

## Discussion

_Reflection on the work done, achievements, challenges faced, limitations, and potential improvements._

## References

_Report References_
_Code References_

## Appendices

_Any appendices go here_

## Pun for good measure

I watched a movie about databases today and now I can't wait for the SQL!

P.S Thanks for a good semester :)