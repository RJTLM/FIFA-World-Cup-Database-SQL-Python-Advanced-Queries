# DSFinalAssignment

## Introduction

This repository contains the implementation of a database system designed to store and query data related to the FIFA Women's World Cup. The project is structured to demonstrate the application of advanced SQL features, such as stored procedures and triggers, and includes a programming language interface to connect to the database.

## Repository Structure

The repository is organized into directories and files that cover various aspects of the database system for the FIFA Women's World Cup. Here is a detailed breakdown:

- `Data/`: Contains CSV files with match data.
  - [`matches_1991_2023.csv`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Data/matches_1991_2023.csv): Match data from 1991 to 2023.

- `ERModelling/`: Includes files related to the Entity-Relationship (ER) model of the database.
  - [`ERDiagram.drawio`](https://github.com/RJTLM/DSFinalAssignment/blob/main/ERModelling/ERDiagram.drawio): Editable ER diagram source file for draw.io.
  - [`ERDiagram.png`](https://github.com/RJTLM/DSFinalAssignment/blob/main/ERModelling/ERDiagram.png): ER diagram image file.
  - [`ERDiagram.xml`](https://github.com/RJTLM/DSFinalAssignment/blob/main/ERModelling/ERDiagram.xml): XML file containing ER diagram data.
  - [`ERDiagramTransparent.png`](https://github.com/RJTLM/DSFinalAssignment/blob/main/ERModelling/ERDiagramTransparent.png): Transparent background version of the ER diagram.

- `Program/`: Contains SQL scripts and Python programs for database operations.
  - `Concepts/`: SQL scripts for database concepts like stored procedures, views, and indexes.
    - [`callGetAverageAttendanceByYear.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/callGetAverageAttendanceByYear.sql): Calls a stored procedure to get average attendance by year.
    - [`callGetTotalMatchesByTeam.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/callGetTotalMatchesByTeam.sql): Calls a stored procedure to get total matches by team.
    - [`explainIdxDateAttendance.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/explainIdxDateAttendance.sql): Explains index usage for MatchDate and Attendance.
    - [`explainIdxTeamName.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/explainIdxTeamName.sql): Explains index usage for TeamName.
    - [`indexes.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/indexes.sql): SQL script for creating indexes.
    - [`selectViewMatchAttendanceSummary.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/selectViewMatchAttendanceSummary.sql): Selects from the view for match attendance summary.
    - [`selectViewTopScorers.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/selectViewTopScorers.sql): Selects from the view for top scorers.
    - [`storedProcedures.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/storedProcedures.sql): SQL script for stored procedures.
    - [`views.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Concepts/views.sql): SQL script for creating views.
  - `Queries/`: SQL scripts for basic and advanced queries.
    - [`advancedQueries.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Queries/advancedQueries.sql): SQL script for advanced queries.
    - [`basicQueries.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Queries/basicQueries.sql): SQL script for basic queries.
  - `Tables/CreateTables/`: SQL scripts for creating the database and tables.
    - [`createDatabase.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Tables/CreateTables/createDatabase.sql): SQL script for creating the database.
    - [`createRelationshipSets.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Tables/CreateTables/createRelationshipSets.sql): SQL script for creating relationship sets.
    - [`createTablesWithFKDep.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Tables/CreateTables/createTablesWithFKDep.sql): SQL script for creating tables with foreign key dependencies.
    - [`createTablesWithoutFKDep.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Tables/CreateTables/createTablesWithoutFKDep.sql): SQL script for creating tables without foreign key dependencies.
    - [`deleteDatabase.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Tables/CreateTables/deleteDatabase.sql): SQL script for deleting the database.
    - [`useDatabase.sql`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/Tables/CreateTables/useDatabase.sql): SQL script to select the database for use.
  - Python scripts for interfacing with the database.
    - [`mySQLConnector.py`](https://github.com/RJTLM/DSFinalAssignment/blob/main/Program/mySQLConnector.py): Python script for MySQL database connection.
    - Other Python scripts for data manipulation and execution of database operations.

- [`README.md`](https://github.com/RJTLM/DSFinalAssignment/blob/main/README.md): The README file provides an introduction and guide to the repository.


## Part 1: Database Design

### ER Modeling

The ER diagram, following Chen's notation, identifies entities, attributes, relationships, cardinality, and participation constraints. It is designed to model the complex scenarios of the FIFA Women's World Cup data.

### Relational Schema

The relational schema is derived from the ER model, ensuring that all tables are normalized to at least the third normal form. The schema includes primary and foreign keys, and other constraints to maintain referential integrity.

### Data Description

Each attribute in the database is defined with a suitable data type and constraints, such as `NOT NULL`. Business rules and attribute descriptions are provided to ensure clarity and consistency.

## Part 2: Database Implementation

### Implementation

The database is implemented in MySQL, with the creation of a sample database named `fifa_womens_world_cup_21171466`. All tables are created with proper constraints to ensure data integrity.

### Loading Sample Data

Sample data is inserted into the database, demonstrating the enforcement of integrity constraints. The data represents a reasonable amount of information to enable meaningful query results.

## Part 3: Queries

### Basic Queries

Basic SQL SELECT statements are used to retrieve data, including numeric, date-time functions, string comparison, and manipulation.

### Advanced Queries

Joins, sub-queries, GROUP BY, ORDER BY, and aggregate functions are used to construct more complex queries.

## Part 4: Advanced Database Features

Advanced database programming concepts are implemented to enhance the database's capabilities. This includes:

- Stored Procedures: For encapsulating complex SQL queries.
- Views: For simplifying complex queries and improving performance.
- Indexes: To speed up the retrieval of records.

## Part 5: Programming Language Interface

The database is connected to a Python3 environment, demonstrating the execution of queries and database operations such as insert, update, and delete through a programming interface.

## User Guide

To run this program:

1. Ensure you have the necessary software, packages and libraries installed including 'python3 -m pip install mysql-connector-python==8.0.5' and 'python3 -m pip install unidecode'
3. Execute the SQL scripts in the `Program/Tables/CreateTables/` directory to create the database and tables.
4. Load sample data using the scripts provided in the `Program/Tables/CreateTables/` directory.
5. Run queries using the scripts in the `Program/Queries/` directory to retrieve data.
6. Explore advanced database features by executing scripts in the `Program/Concepts/` directory.
7. Connect to the database using the provided Python scripts to perform operations programmatically.

## Reflection

The documentation includes a reflection on the design and implementation decisions, challenges faced, and suggestions for improvement based on modern database concepts.
