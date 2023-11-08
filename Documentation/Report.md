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

In this report, I present an overview of the work I have done to design, implement, and query a database system designed for Scenario A, The FIFA Women's World Cup. The entire program can be operated running `python3 ./Program/menu.py` in a linux command-line interface (CLI) (i.e. a terminal in the Virtual Desktop). No direct MySQL database access is required.

Throughout this project, I treated the lecture slides like my bible to design an entity-relationship (ER) model, implement the relational schema, and populate a database with sample data from the csv filed available in Blackboard. I also created and executed a suite of SQL queries, using advanced features such as stored procedures and views to enhance the database's functionality. The culmination of these efforts (along with the fact that I am unfortunately a perfectionist) is a system that meets most of the specified requirements and also demonstrates the practical application of modern database concepts.

I have documented the entire process, reflecting on the design and implementation decisions, identifying challenges, and suggesting improvements should I attempt something similar in the future. This documentation serves as a 'lens' into the numerous hours spent testing, refactoring, and debugging to ensure the delivery of a high-quality database system via Python.

### GitHub and Version Control

I used GitHub to document this project so if you are interested in a more chronological view of the development of my project, you are welcome to review my `private GitHub repository` (happy to give access just don't want to compromise academic integrity), which contains 202 commits at the time of writing and highlight the pain I experienced during testing and refactoring, refactoring and testing, and then testing some more (and also the evolution of this assignment).

[GitHub Repository: RJTLM/DSFinalAssignment](https://github.com/RJTLM/DSFinalAssignment)

By doing this assignment I have been able to apply theoretical knowledge learned in class to a real-world scenario, and the following sections highlight the processes and methodologies used to achieve the objectives herein.


## Design of the Database

### Entity Selection

The design of the database for the FIFA Women's World Cup evolved over numerous iterations and careful consideration was given to the selection of entities, their relationships and cardinality.

#### Entities and Attributes

The entities for this database are `Match`, `Team`, `Player`, `Event`, `Manager`, and `Referee`. These entities are central components of the tournament and are described as follows:

- **Match**: Represents individual games played within the tournament. Attributes include unique identifiers, scores, penalties, attendance, venue, and related event information. The `MatchID` serves as the primary key, ensuring each match is uniquely identifiable.
  
- **Team**: Captures the teams participating in the World Cup. The `TeamName` is the primary key and is used to link players and matches to teams.
  
- **Player**: Details the players, including whether they are a team captain. The `PlayerName` is the primary key, and the `isCaptain` attribute is a boolean indicating captaincy.
  
- **Event**: Represents tournament data, with year, host, number of teams, and outcomes such as the champion and top scorer as attributes. The `EventID` is the primary key.
  
- **Manager**: Contains information on team managers. The `ManagerName` is the primary key.
  
- **Referee**: Contains information on the primary match referees. The `RefereeName` is the primary key.

#### Relationships

These relationships between entities are critical to the design:

- **Plays**: A many-to-many relationship between `Match` and `Team`, demonstrating which teams play in which matches. Attributes include `MatchID`, `TeamName`, and `HomeAway` to indicate whether the team is playing at home or away (this is how data is presented in the csv file).
  
- **Manages**: A many-to-many relationship between `Match` and `Manager`, indicating which manager manages a team in a particular match.
  
- **PlaysFor**: A many-to-many relationship between `Player` and `Team`, indicating which players play for which teams.
  
- **IsPlayedIn**: A one-to-many relationship between `Match` and `Event`, linking matches to the event they are part of.

#### Data Types

Data types were chosen based on my understanding of what best represents the nature of the data:

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

- **Mandatory Participation**: An entity must participate in the relationship, such as every match must be associated with an event.
  
- **Optional Participation**: An entity's participation in the relationship is not required, such as a player not needing to be a captain.

The entity selection and relationship mapping were done with the intention of creating a database that is as reflective of the real-world as possible, and is also user-friendly with regards to query performance and data integrity. 

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

The chosen data types and constraints ensure that the database is normalized to reduce redundancy and improve data consistency:

#### First Normal Form (1NF)
For a table to be in 1NF, it must have:
1. No repeating groups or arrays.
2. All values must be atomic (indivisible).

My Schema:
- Each attribute has atomic values (no multi-valued attributes).
- There are no repeating groups; for example, `Plays` and `Manages` are separate tables, showing my many-to-many relationships are handled correctly.

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
15. **Tournament Data Focus**: The database is primarily focused on capturing and providing insights into tournament-level data, such as match outcomes, team progress, and crowd attendance. It is not designed to analyse internal match statistics beyond standard information such as the winner, loser, scores, and basic event occurrences.

## Implementation of the Database and Adding Sample Data

### Database Implementation

My  goal for this project was to have everything run via a Python program and not need to directly access the database via MySQL.

The first thing I needed to do was clean the provided CSV files. A lot of the data (particuarly player names) had non-ASCII characters so I created `asciiConversion.py`, a script that cleaned and converted non-ASCII characters to their ASCII equivalents.

Following this, I built `dataViewer.py`. This program allowed users to view the contents of CSV files directly through the CLI so applications such as Excel were not needed.

`extractData.py` was designed to extract only the essential columns required for database insertion. This script allowed me to extract the data I wanted with the intent of minimising potential issues later on.

I then created `splitColumn.py` when I was still planning to insert detailed player data into the database. This changed as I progressed through the assignment but kept the program there as a useful tool nonetheless. If I had more time, I would have refactored this script to better split columns with multiple delimiters, etc..

`menu.py` is the central script that runs the entire program. It has a user-friendly menu system, allowing for easy navigation and operation of the various functionalities, all from within the terminal.

Once I was satisfied that I had useable data, I focused on the database implementation. `mySQLConnector.py` is the entry point that facilitates database connection upon user authentication (hidden password too).

The database's construction was broken down into smaller pieces and involved a series of Python scripts and SQL files. `createTables.py` laid the foundation, `createDatabase.sql`, `useDatabase.sql`, `createTablesWithoutFKDep.sql`, `createTablesWithFKDep.sql`, and `createRelationshipSets.sql` all functioned to create the database and tables. It is worth noting that the tables without any dependencies were created first, then tables with dependencies and then relationship (many-to-many) tables (I figured this out the hard way).

During testing, I created `deleteDatabase.sql` as a means to quickly reset the database without needing to do so via MySQL. Although this would not likely be included in a real-world application (not to the extremity of its function), a more comprehensive version likely would so I chose to keep it in my final design.

### Sample Data and Insertion

This phase of the project was for me, without a doubt, the most challenging and time-consuming. I kept getting stuck, diving deep into the online void of data insertion (thanks Google), and making thinks more difficult than they needed to be. There wasn't much detail in the lecture slides about to insert data from CSV files directly into MySQL (via Python) tables led me down a path of overly-extensive research and reiteration.

Initially, I attempted to create a comprehensive table that could hold all CSV data by using `createBigDataTable.sql` and `insertBigData.sql` (these is no longer available unless you want to find them in my version control history). This approach hit a dead end when I realized it wasn't feasible. It was during this period of trial and error that I decided to narrow the scope of my database to focus solely on tournament data, as the player information provided in the CSV files was causing numerous issues due to its format (multiple pieces of data in each column that I struggled to accurately extract).

After going around in circles, I discovered that Python could in fact be used to insert data directly into each table (even though this is what I initiall tried to do), bypassing the need for intermediary SQL scripts. This resulted in the final version of `insertData.py`, a script that became the central piece of code for data insertion.

`insertData.py` clears any existing data in the tables to ensure a clean slate for insertion (I know this would likely function differently in a real-world scenario). The script then inserts data into the tables documented above. It uses a combination of `INSERT` and `INSERT IGNORE` statements to add new records while avoiding duplicates (teamName, etc.).

The script handles exceptions in detail and reports any errors encountered during the insertion process. Upon successful insertion, it commits the changes to the database and confirms the completion of the operation.

## Use of the Database

### Queries

#### Implementation of Database Queries via `queries.py`

The purpose of creating `queries.py` was to streamline the process of executing SQL queries against the database without needing to access the database via MySQL (as mentioned earlier in this report). The script allows users to view the predefined queries (see below) by selecting options from a menu and then being provided the data outputed in the CLI.

The queries were created in SQL files and `queries.py` reads those files. Furthermore, the output is presented in a tabular form, making the data accessible and straightforward to interpret (although this isn't going to be perfect without adding additional libraries which is beyond the scope of this task).

#### Basic Queries

##### Find all matches played by a specific team (Sweden):

```sql
SELECT FM.* FROM FootballMatch FM
JOIN Plays P ON FM.MatchID = P.MatchID
WHERE P.TeamName IN ('Sweden');
```

TThis is a SELECT statement combined with an INNER JOIN that retrieves all records from the FootballMatch table where the team 'Sweden' participated. It uses a string comparison in the WHERE clause to filter the results. This demonstrates basic methods of joining tables and filtering with suitable WHERE clauses.

##### Retrieve all matches with attendance greater than 50,000:

```sql
SELECT * FROM FootballMatch WHERE Attendance > 50000;
```

This query is a SELECT statement that uses a numeric comparison in the WHERE clause to select matches from the FootballMatch table with attendance figures exceeding a certain threshold, showcasing the use of numeric data in conditions.

##### Get details of matches played in August 2023:

```sql
SELECT * FROM FootballMatch WHERE MatchDate BETWEEN '2023-08-01' AND '2023-08-31';
```

Here, a SELECT statement is used with a date-time function, BETWEEN, to extract matches within a specific date range, illustrating the use of date-time functions in SQL queries. The purpose of this query is to extract all matches that took place in the month of August 2023.

##### Find all matches where the home team scored more than 2 goals:

```sql
SELECT * FROM FootballMatch WHERE home_score > 2;
```

This query employs a SELECT statement with a numeric condition in the WHERE clause to find matches with high home team scores (more than 2 goals), again using numeric data comparisons.

##### Retrieve all matches refereed by a specific referee (Tori Penso):
```sql
SELECT * FROM FootballMatch WHERE RefereeName = 'Tori Penso';
```

A SELECT statement with a string comparison in the WHERE clause is used to filter matches based on the referee's name, showcasing string comparison and manipulation in SQL.

#### Advanced Queries

My advanced queries use `COUNT()`, `AVG()`, and `SUM()`, and involve grouping and ordering results to extract meaningful statistics and trends.

##### Total Number of Matches Played by Each Team:

```sql
SELECT TeamName, COUNT(*) as TotalMatches FROM Plays GROUP BY TeamName ORDER BY TotalMatches DESC;
```

This advanced query is a SELECT statement that uses the GROUP BY clause in conjunction with an aggregate function, COUNT(), and orders the results using ORDER BY. It demonstrates the ability to group data and calculate aggregate values. This query calculates the total number of matches played by each team.

##### Average Attendance of Matches for Each Venue:

```sql
SELECT Venue, AVG(Attendance) as AvgAttendance FROM FootballMatch WHERE Attendance IS NOT NULL GROUP BY Venue ORDER BY AvgAttendance DESC;
```

Here, the query uses a SELECT statement with the GROUP BY clause and an aggregate function, AVG(), to calculate the average. It also includes a WHERE clause to exclude null values, and it uses ORDER BY to sort the results, illustrating the use of aggregate functions and related clauses. By excluding null values, we ensure accuracy in our calculations.

##### Top Scorer of Each Event:

```sql
SELECT EventID, TopScorer FROM Event WHERE TopScorer IS NOT NULL;
```

This query is a SELECT statement with a string comparison in the WHERE clause to filter non-null values, focusing on string data manipulation.

##### Total Number of Goals Scored in Each Round of the 2023 Event:

```sql
SELECT Round, SUM(home_score + away_score) as TotalGoals FROM FootballMatch WHERE EventID = 9 GROUP BY Round ORDER BY TotalGoals DESC;
```

An advanced SELECT statement that combines the GROUP BY clause with an aggregate function, SUM(), and uses ORDER BY to sort the results. It demonstrates complex data aggregation and ordering of the total goals scored in each round of the 2023 World Cup event.

##### Matches Where Penalty Kicks Were Taken in the 2023 Event:

```sql
SELECT FM.* FROM FootballMatch FM JOIN Event E ON FM.EventID = E.EventID WHERE (home_penalty IS NOT NULL OR away_penalty IS NOT NULL) AND E.EventYear = 2023;
```

This query is a complex SELECT statement that uses an INNER JOIN to combine data from two tables and employs the WHERE clause with a logical OR to filter matches based on penalty kicks. It showcases the use of joins, sub-queries, and conditional logic.

### Advanced Features

#### Advanced Features Implementation and Troubleshooting

`concepts.py` and `executeConcepts.py`, interact with the advanced SQL features I had implemented in my database. The `concepts.py` script was designed to load and execute SQL commands for stored procedures, views, and indexes from the corresponding SQL files. It used regular expressions to parse the SQL commands and a menu to allow users to select which SQL concept to load and execute.

The `executeConcepts.py` script, on the other hand, was focused on executing predefined SQL concepts. It read SQL commands from files and executed them using a cursor object from the MySQL connector.

Unfortunately, I encountered errors when attempting to call the advanced features from these Python scripts. The program looped back to the menu without crashing but the advanced features did not work as intended. I would have implemented delimiters in a direct MySQL environment to avoid such problems and fatigue is probably the reason I had so many issues that are likely very solvable.

#### Stored Procedures

- **GetTotalMatchesByTeam**: This procedure was supposed to count the matches played by a specific team. It was just a call away from providing quick insights. However, when I tried to call it from via Python application, it resulted in errors.

   ```sql
   CREATE PROCEDURE GetTotalMatchesByTeam(IN teamName VARCHAR(255))
   BEGIN
       SELECT TeamName, COUNT(*) as TotalMatches 
       FROM Plays 
       WHERE TeamName = teamName
       GROUP BY TeamName;
   END;

My attempt to invoke it: `CALL GetTotalMatchesByTeam('Sweden');`

- **GetAverageAttendanceByYear**: Aimed at calculating average attendance figures, this procedure was meant to make it easier to pull out relevant attendance data.

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

#### Views

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

- **idx_teamname**: I expected this index to improve search performance on the `TeamName` field in the `Plays` table.

```sql
CREATE INDEX idx_teamname ON Plays(TeamName);
```

- **idx_date_attendance**: By indexing `MatchDate` and `Attendance`, I aimed to make queries filtered by these fields faster.

```sql
CREATE INDEX idx_date_attendance ON FootballMatch(MatchDate, Attendance);
```

I planned to use `EXPLAIN` statements to demonstrate the performance improvements with these indexes.

### Database Connectivity and Python Implementation

#### Database Connection

I used the `mysql.connector` library to establish a connection between the Python application and the database:

```python
# mySQLCOnnector.py
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

The connection process prompts the user for their MySQL username and password and then uses these credentials to establish a connection.

#### Python Scripts for Database Interaction

As previously notes, my goal for this project was to successfully implement the entire assignment in Python, create a comprehensive menu system and integrate advanced features that would allow users to connect to and interact with the FIFA Women's World Cup database via the command-line interface (CLI).

From the outset, my vision was to create a system that exceeded the project's requirements. This system was designed to facilitate every operation detailed in the assignment brief through the CLI to avoid direct MySQL database interaction.

`asciiConversion.py`, addressed the challenge of non-ASCII characters in player names by ensuring compatibility across the system. `dataViewer.py` allowed users to view CSV files directly through the CLI, and `extractData.py` streamlined the process of extracting essential data for database insertion (although this could have been better).

`menu.py` is a user-friendly menu system and is the gateway to the other functionalities I created

`mySQLConnector.py` allows for database connection. `createTables.py`, `createDatabase.sql`, `useDatabase.sql`, `createTablesWithoutFKDep.sql`, `createTablesWithFKDep.sql`, `createRelationshipSets.sql`, and others were methodically executed to construct the database's structure and relationships.

In summary, each script and SQL file played a pivotal role in building a user-friendly system that simplified the management of databases without the need for direct MySQL access.

#### Error Handling and Security

##### Error Handling

Error handling in Python is managed using try-except blocks. When interacting with the MySQL database, the `mysql.connector.Error` exception is used to handle any issues that may arise during database operations, as used in `insertData.py`. Each database's insertion operation is wrapped in a try-except block to catch and handle any errors that occur:

```python
# insertData.py
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
#queries.py
try:
    cursor.execute(query, params)
    records = cursor.fetchall()
    return records
except Exception as e:
    print("Error reading data from MySQL table", e)
```

##### Security

Security during database interactions is primarily concerned with preventing unauthorized access and SQL injection attacks. `mySQLConnector.py` prompts the user for their MySQL username and password, which are not stored in the script:

```python
#mySQLConnector.py
db_config = {
        'host': 'localhost',
        'user': input("\nEnter your MySQL username: "),
        'password': getpass.getpass("Enter your MySQL password: "),
    }
```

## Discussion

I am proud of the Python application I created. It intergrates with a MySQL database for the FIFA Women's World Cup (my first Python program). I successfully implementing a comprehensive menu system that allows users to interact with the database via the CLI. In the real world, this feature would make the database more accessible to users who may not be familiar with SQL syntax, although I understand there are better still practices that I will learn about in future untis.

Even though I had diffulcities with data insertion and advanced concepts, I managed to create a Python program that achieved most objectives set out in the assignment brief.

In terms of potential improvements (if I had more time), the error handling could be more sophisticated, and the security measures could always be strengthened. Additionally, the user interface could be made more intuitive, and the documentation could be expanded to provide clearer guidance for future users.

Overall, this project has been a valuable learning experience. I am eager to build on this foundation, refining the application and expanding its capabilities in future iterations.

## References

### Report References
DS Lecture Slides Semester 2 2023.

### Code References

All sources of information I used to implement my database was referenced directly in the code where applicable. This is my first time using Python for an assignment so needed to use numerous sources to complete the project. I apologise if I used strategies or techniques that are not completely conventional. I also apologise if I 'over-referenced'.

## Pun for good measure

I watched a movie about databases today and now I can't wait for the SQL!

P.S Thanks for a good semester :)