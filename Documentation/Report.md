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

In this section, I will detail the design and implementation of various queries used to interact with the database. These queries range from simple data retrieval to more complex queries.

#### ### Implementation of Database Queries via `queries.py`

In developing queries.py, my intention was to streamline the process of executing SQL queries against the database database (as mentioned earlier in this report). The script is designed to be intuitive, allowing users to retrieve data with ease by selecting options from a menu.

The script presents a selection of predefined queries. Users can choose from basic to advanced queries, each corresponding to a specific data retrieval function. Upon selection, the script executes the relevant SQL command, fetching and displaying the results in a clear and organized format.

Moreover, the queries are externalized in SQL files for flexibility and maintainability. Adjustments to queries can be made directly in the SQL files without altering the Python script, facilitating updates and modifications. The output is presented in a tabular form, making the data accessible and straightforward to interpret.

#### Basic Queries

##### Find all matches played by a specific team (Sweden):

```sql
SELECT FM.* FROM FootballMatch FM
JOIN Plays P ON FM.MatchID = P.MatchID
WHERE P.TeamName IN ('Sweden');
```

TThis is a SELECT statement combined with an INNER JOIN that retrieves all records from the FootballMatch table where the team 'Sweden' participated. It uses a string comparison in the WHERE clause to filter the results, demonstrating basic methods of joining tables and filtering with suitable WHERE clauses. This information is useful for analyzing the performance and schedule of the Swedish team, and it provides a focused dataset for anyone specifically interested in this team's matches.

##### Retrieve all matches with attendance greater than 50,000:

```sql
SELECT * FROM FootballMatch WHERE Attendance > 50000;
```

This query is a simple SELECT statement that uses a numeric comparison in the WHERE clause to select matches from the FootballMatch table with attendance figures exceeding a certain threshold, showcasing the use of numeric data in conditions. The result set from this query is important for identifying highly attended matches, which could be indicative of high-profile games or venues with significant capacity. This data can be used for crowd management studies or marketing analysis.

##### Get details of matches played in August 2023:

```sql
SELECT * FROM FootballMatch WHERE MatchDate BETWEEN '2023-08-01' AND '2023-08-31';
```

Here, a SELECT statement is used with a date-time function, BETWEEN, to extract matches within a specific date range, illustrating the use of date-time functions in SQL queries. The purpose of this query is to extract all matches that took place in the month of August 2023. It's useful for generating reports on matches played within a specific time frame, possibly for monthly summaries or tournament analysis.

##### Find all matches where the home team scored more than 2 goals:

```sql
SELECT * FROM FootballMatch WHERE home_score > 2;
```

This query employs a SELECT statement with a numeric condition in the WHERE clause to find matches with high home team scores (more than 2), again using numeric data comparisons. It's a valuable query for understanding which home teams have a strong offensive performance, and it could be used for statistical analysis of home advantage or for identifying high-scoring teams.

##### Retrieve all matches refereed by a specific referee (Tori Penso):
```sql
SELECT * FROM FootballMatch WHERE RefereeName = 'Tori Penso';
```

A SELECT statement with a string comparison in the WHERE clause is used to filter matches based on the referee's name, showcasing string comparison and manipulation in SQL. This information might be used to review the referee's workload, distribution of matches, or to analyze the matches they have overseen for performance and decision-making patterns.

#### Advanced Queries

In this section, I delve into the more sophisticated queries that provide deeper insights into the dataset. These advanced queries leverage SQL functions like `COUNT()`, `AVG()`, and `SUM()`, and involve grouping and ordering results to extract meaningful statistics and trends.

##### Total Number of Matches Played by Each Team:

```sql
SELECT TeamName, COUNT(*) as TotalMatches FROM Plays GROUP BY TeamName ORDER BY TotalMatches DESC;
```

This advanced query is a SELECT statement that uses the GROUP BY clause in conjunction with an aggregate function, COUNT(), and orders the results using ORDER BY. It demonstrates the ability to group data and calculate aggregate values. This query calculates the total number of matches played by each team, giving us a clear picture of team activity. Teams are grouped and ordered by the total number of matches they've played, descending from the most active team. This helps in analyzing team participation across events.

##### Average Attendance of Matches for Each Venue:

```sql
SELECT Venue, AVG(Attendance) as AvgAttendance FROM FootballMatch WHERE Attendance IS NOT NULL GROUP BY Venue ORDER BY AvgAttendance DESC;
```

Here, the query uses a SELECT statement with the GROUP BY clause and an aggregate function, AVG(), to calculate the average. It also includes a WHERE clause to exclude null values, and it uses ORDER BY to sort the results, illustrating the use of aggregate functions and related clauses. By excluding null values, we ensure accuracy in our calculations. This data can be pivotal for venue management and event planning, and also forecasting for future World Cup tournaments.

##### Top Scorer of Each Event:

```sql
SELECT EventID, TopScorer FROM Event WHERE TopScorer IS NOT NULL;
```

This query is a straightforward SELECT statement with a string comparison in the WHERE clause to filter non-null values, focusing on string data manipulation. Identifying the top scorer for each event is crucial for recognizing outstanding individual performances. This query filters out events without a top scorer to concentrate on those with clear leading players.

##### Total Number of Goals Scored in Each Round of the 2023 Event:

```sql
SELECT Round, SUM(home_score + away_score) as TotalGoals FROM FootballMatch WHERE EventID = 9 GROUP BY Round ORDER BY TotalGoals DESC;
```

An advanced SELECT statement that combines the GROUP BY clause with an aggregate function, SUM(), and uses ORDER BY to sort the results. It demonstrates complex data aggregation and ordering of the total goals scored in each round of a specific event (in this case, the 2023 event). It's an excellent tool for analyzing the progression of the event in terms of scoring, which can reflect the intensity of competition in different stages.

##### Matches Where Penalty Kicks Were Taken in the 2023 Event:

```sql
SELECT FM.* FROM FootballMatch FM JOIN Event E ON FM.EventID = E.EventID WHERE (home_penalty IS NOT NULL OR away_penalty IS NOT NULL) AND E.EventYear = 2023;
```

This query is a complex SELECT statement that uses an INNER JOIN to combine data from two tables and employs the WHERE clause with a logical OR to filter matches based on penalty kicks. It showcases the use of joins, sub-queries, and conditional logic. This is particularly interesting for studying matches that were closely contested and may have required penalties to determine the outcome.

### Advanced Features

#### Advanced Features Implementation and Troubleshooting

In my project, I developed two Python scripts, `concepts.py` and `executeConcepts.py`, to interact with the advanced SQL features I had implemented in my database. The `concepts.py` script was designed to load and execute SQL commands for stored procedures, views, and indexes from corresponding SQL files. It used regular expressions to parse the SQL commands and an interactive execution function to allow users to select which SQL concept to load and execute. This script was crucial for testing the functionality of the advanced features within the Python environment.

The `executeConcepts.py` script, on the other hand, was focused on executing predefined SQL concepts. It read SQL commands from files and executed them using a cursor object from the MySQL connector. This script was intended to facilitate the direct execution of complex SQL operations such as calling stored procedures and creating views, with the added functionality of explaining indexes to assess their impact on query performance.

Despite my efforts to ensure smooth integration, I encountered errors when attempting to call the advanced features from these Python scripts. Although the SQL syntax was correct, and the program looped back to the menu without crashing, the advanced features did not work as intended. This was a setback, as I had not anticipated such issues, especially since I would have implemented delimiters in a direct MySQL environment to avoid such problems. The experience underscored the challenges of interfacing SQL with external programming languages, and it became clear that I needed to delve deeper into troubleshooting to achieve the desired functionality.

#### Stored Procedures

I implemented stored procedures to simplify complex operations, enabling them to be executed repeatedly with just a command. This approach made data management more efficient and also improved security by limiting direct user access to the data.

- **GetTotalMatchesByTeam**: This procedure was supposed to count the matches played by a specific team. It was just a call away from providing quick insights. However, when I tried to invoke it from my Python application, it resulted in errors.

   ```sql
   CREATE PROCEDURE GetTotalMatchesByTeam(IN teamName VARCHAR(255))
   BEGIN
       SELECT TeamName, COUNT(*) as TotalMatches 
       FROM Plays 
       WHERE TeamName = teamName
       GROUP BY TeamName;
   END;

My attempt to invoke it: `CALL GetTotalMatchesByTeam('Sweden');`

- **GetAverageAttendanceByYear**: Aimed at calculating average attendance figures, this procedure was meant to make it easier to pull out relevant attendance data. Like the first, it encountered issues when executed through the Python interface.

```sql
CREATE PROCEDURE GetAverageAttendanceByYear(IN year INT)
BEGIN
    SELECT Venue, AVG(Attendance) as AvgAttendance 
    FROM FootballMatch 
    WHERE YEAR(MatchDate) = year AND Attendance IS NOT NULL 
    GROUP BY Venue;
END;
```

My attempt to invoke it: `CALL GetAverageAttendanceByYear(2023);`

I had expected these procedures to run smoothly since they were syntactically correct. If I had been working directly in MySQL, I would have included delimiters for proper statement termination. However, the Python MySQL connector should handle these without needing explicit delimiter statements. The errors were unexpected, but thankfully, my program was robust enough to catch exceptions and continue running, allowing for a seamless user experience.

#### Views

I set up views to offer a simplified and efficient way to access complex query results. They functioned well within the database (when the delimiters were included), but the real test was accessing them through the Python program.

- **ViewTopScorers**: This view was meant to highlight top performers easily, without the need for complex joins or subqueries.

```sql
CREATE VIEW ViewTopScorers AS
SELECT EventID, TopScorer
FROM Event
WHERE TopScorer IS NOT NULL;
```

- **ViewMatchAttendanceSummary**: This view was designed to provide a quick overview of attendance statistics, aggregating and averaging the data by venue.

```sql
CREATE VIEW ViewMatchAttendanceSummary AS
SELECT Venue, AVG(Attendance) as AvgAttendance
FROM FootballMatch
WHERE Attendance IS NOT NULL
GROUP BY Venue;
```

#### Indexes

I chose indexes to speed up data retrieval, an essential part of performance tuning, especially as data volumes grow.

- **idx_teamname**: I expected this index to improve search performance on the `TeamName` field in the `Plays` table.

```sql
CREATE INDEX idx_teamname ON Plays(TeamName);
```

- **idx_date_attendance**: By indexing `MatchDate` and `Attendance`, I aimed to make queries filtered by these fields faster.

```sql
CREATE INDEX idx_date_attendance ON FootballMatch(MatchDate, Attendance);
```

I planned to use `EXPLAIN` statements to demonstrate the performance improvements with these indexes.

Even with careful planning and implementation, the advanced features didn't work as seamlessly as I hoped when called from the Python application. This experience has shown me the intricacies of integrating SQL with external programming languages. I'm now focused on troubleshooting these issues to ensure that the advanced features are just as effective through the Python application as they are within the MySQL environment.

### Database Connectivity and Python Implementation

#### Database Connection

To establish a connection between the Python application and the database, I utilised the `mysql.connector` library. This library provides an interface for connecting to a MySQL database server from Python. Below is an example of how the connection is set up:

```python
import mysql.connector
import getpass

def connect_to_db():
    # Database configuration
    db_config = {
        'host': 'localhost',
        'user': input("\nEnter your MySQL username: "),
        'password': getpass.getpass("Enter your MySQL password: "),
        # Uncomment the following line and replace with your database name
        # 'database': 'your_database_name_here'
    }

    # Establish a database connection
    db_connection = mysql.connector.connect(**db_config)
    cursor = db_connection.cursor()

    print("\nConnection established!")
    return cursor, db_connection
```

The connection process involves prompting the user for their MySQL username and password and then using these credentials to establish a connection. The connect_to_db function encapsulates this process and returns both the connection object and cursor for executing SQL commands.

#### Python Scripts for Database Interaction

My goal for this project was to successfully implement the entire assignment in Python, create a comprehensive menu system and integrate advanced features that would allow users to connect to and interact with the FIFA Women's World Cup database via the command-line interface (CLI).

From the outset, my vision was to create a system that exceeded the project's requirements. This system was designed to facilitate every operation detailed in the assignment brief through the CLI, thereby negating the need for direct MySQL database interaction. This approach was intended to simplify the user experience, making database management more accessible and intuitive.

The journey began with the development of `asciiConversion.py`, a script that addressed the challenge of non-ASCII characters in player names by ensuring compatibility across the system. This was followed by the creation of `dataViewer.py`, which allowed users to inspect CSV files directly through the CLI, and `extractData.py`, which streamlined the process of extracting essential data for database insertion.

Recognizing the complexity of the task, I developed `splitColumn.py` to fully utilize the CSV data. However, I soon realized that this script, while functional, was more complex than necessary for the project's scope. The experience underscored the importance of balancing ambition with practicality.

The backbone of the user experience was `menu.py`, a script that provided a user-friendly menu system. This script was the gateway to the suite of tools, enabling users to navigate and operate various functionalities seamlessly within the CLI.

The database implementation itself was a phased operation, with `mySQLConnector.py` serving as the entry point for database connection. A series of scripts and SQL files, including `createTables.py`, `createDatabase.sql`, `useDatabase.sql`, `createTablesWithoutFKDep.sql`, `createTablesWithFKDep.sql`, and `createRelationshipSets.sql`, were methodically executed to construct the database's structure and relationships.

Moreover, `deleteDatabase.sql` was an essential tool for resetting the database, which proved invaluable for testing and refining the system to ensure its robustness.

In summary, each script and SQL file played a pivotal role in building a user-friendly system that simplified the management of databases without the need for direct MySQL access.

#### Error Handling and Security

In the context of database interactions within the project, error handling and security are implemented through several methods:

##### Error Handling

Error handling in Python is managed using try-except blocks. When interacting with the MySQL database, the `mysql.connector.Error` exception is specifically caught to handle any issues that may arise during database operations. This is evident in the `insertData.py` script, where each database insertion operation is wrapped in a try-except block to catch and handle any errors that occur.

For example, when inserting data into the Event table:

```python
try:
    # Insert data into the Event table from littleDataCleaned.csv
    # ...
    db_connection.commit()
    print("Data successfully inserted into the Event table.")
except Error as e:
    print(f"Error inserting into Event: {e}")
    all_insertions_successful = False
```

Similarly, the `queries.py` script uses exception handling to manage errors that may occur when executing SQL queries:

```python
try:
    cursor.execute(query, params)
    records = cursor.fetchall()
    return records
except Exception as e:
    print("Error reading data from MySQL table", e)
```

##### Security

Security during database interactions is primarily concerned with preventing unauthorized access and SQL injection attacks. The `mySQLConnector.py` script demonstrates a secure method of connecting to the database by prompting the user for their MySQL username and password, which are not stored in the script:

```python
db_config = {
    'host': 'localhost',
    'user': input("\nEnter your MySQL username: "),
    'password': getpass.getpass("Enter your MySQL password: "),
    # 'database': 'your_database_name_here'
}
```

Furthermore, the use of parameterized queries is a good practice to prevent SQL injection, as it ensures that any input is treated as a parameter rather than part of the SQL statement. This is a security best practice that is observed throughout the project's database interaction scripts.

## Discussion

I am proud of the strides I've made in developing a Python application that interfaces with a MySQL database for the FIFA Women's World Cup (my first Python program). The journey was marked by significant achievements, such as successfully implementing a comprehensive menu system that allows users to interact with the database through a command-line interface. In the real world, this feature would make the database more accessible to users who may not be familiar with SQL syntax.

One of the main challenges I faced was ensuring the robustness of data handling, particularly when cleaning and inserting the CSV data into the database. The complexity of the data, with its non-ASCII characters and intricate relationships, required attention to detail and innovative scripting solutions that may have taken me slighlty off course.

Despite these challenges, I managed to create a suite of Python scripts that handle data insertion and enable complex queries and database management tasks. The `insertData.py` script stands out as a testament to this effort, efficiently populating the database while handling exceptions to maintain data integrity.

However, the project was not without its limitations. The advanced SQL features, such as stored procedures, views, and indexes, did not integrate as smoothly with the Python application as I had hoped. This highlighted the intricacies of interfacing SQL with external programming languages and has become a focal point for further development.

In terms of potential improvements, the error handling could be more sophisticated, and the security measures could always be strengthened. Additionally, the user interface could be made more intuitive, and the documentation could be expanded to provide clearer guidance for future users.

Overall, this project has been a valuable learning experience, providing insights into the complexities of database management and the power of Python scripting. I am eager to build on this foundation, refining the application and expanding its capabilities in future iterations.

## References

### Report References
DS Lecture Slides Semester 2 2023.

### Code References

All sources of information I used to implement my database was referenced directly in the code where applicable. This is my first time using Python for an assignment so needed to use numerous sources to complete the project. I apologise if I used strategies or techniques that are not completely conventional. I also apologise if I 'over-referenced'.

## Pun for good measure

I watched a movie about databases today and now I can't wait for the SQL!

P.S Thanks for a good semester :)