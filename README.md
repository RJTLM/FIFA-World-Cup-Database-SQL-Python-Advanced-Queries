# DSFinalAssignment

## Introduction

This repository contains the implementation of a database system designed to store and query data related to the FIFA Women's World Cup. The project is structured to demonstrate the application of advanced SQL features, such as stored procedures and triggers, and includes a programming language interface to connect to the database.

## Repository Structure

- `Data/`: Contains CSV files with original match data.
  - `matches_1991_2023.csv`: Match data from 1991 to 2023.
  - `world_cup_women.csv`: Event data.

- `ERModelling/`: Includes files related to the Entity-Relationship (ER) model of the database.
  - `ERDiagram.drawio`: Editable ER diagram source file for draw.io.
  - `ERDiagram.png`: ER diagram image file.
  - `ERDiagram.xml`: XML file containing ER diagram data.
  - `ERDiagramTransparent.png`: Transparent background version of the ER diagram.

- `Program/`: Contains SQL scripts and Python programs for database operations.
  - `Concepts/`: SQL scripts for database concepts like stored procedures, views, and indexes.
    - `callGetAverageAttendanceByYear.sql`: Calls a stored procedure to get average attendance by year.
    - `callGetTotalMatchesByTeam.sql`: Calls a stored procedure to get total matches by team.
    - `explainIdxDateAttendance.sql`: Explains index usage for MatchDate and Attendance.
    - `explainIdxTeamName.sql`: Explains index usage for TeamName.
    - `indexes.sql`: SQL script for creating indexes.
    - `indexes1.sql`: Additional SQL script for creating indexes.
    - `selectViewMatchAttendanceSummary.sql`: Selects from the view for match attendance summary.
    - `selectViewTopScorers.sql`: Selects from the view for top scorers.
    - `storedProcedures.sql`: SQL script for stored procedures.
    - `storedProcedures1.sql`: Additional SQL script for stored procedures.
    - `views.sql`: SQL script for creating views.
    - `views1.sql`: Additional SQL script for creating views.
  - `Queries/`: SQL scripts for basic and advanced queries.
    - `advancedQueries.sql`: SQL script for advanced queries.
    - `basicQueries.sql`: SQL script for basic queries.
  - `Tables/CreateTables/`: SQL scripts for creating the database and tables.
    - `createDatabase.sql`: SQL script for creating the database.
    - `createRelationshipSets.sql`: SQL script for creating relationship sets.
    - `createTablesWithFKDep.sql`: SQL script for creating tables with foreign key dependencies.
    - `createTablesWithoutFKDep.sql`: SQL script for creating tables without foreign key dependencies.
    - `deleteDatabase.sql`: SQL script for deleting the database.
    - `useDatabase.sql`: SQL script to select the database for use.
  - Python scripts for interfacing with the database.
    - `asciiConversion.py`: Python script for ASCII conversion.
    - `concepts.py`: Python script related to database concepts.
    - `createTables.py`: Python script for creating tables.
    - `dataViewer.py`: Python script for viewing data.
    - `executeConcepts.py`: Python script to execute concepts.
    - `extractData.py`: Python script for data extraction.
    - `insertData.py`: Python script for inserting data into the database.
    - `menu.py`: Python script for the menu interface.
    - `mySQLConnector.py`: Python script for MySQL database connection.
    - `queries.py`: Python script for executing queries.
    - `splitColumn.py`: Python script for splitting columns.
    - `updateDatabase.py`: Python script for updating the database.
    - `viewData.py`: Python script for viewing data.

- `README.md`: The README file provides an introduction and guide to the repository.

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

Based on the content of the `menu.py` script and the `README.md` file from the repository, the user guide can be updated to reflect the actual flow of the program. Here is the revised user guide:

## User Guide

To run this program:

1. Ensure you have the necessary software, packages, and libraries installed including:
   - Python 3
   - MySQL Connector for Python: Run `python3 -m pip install mysql-connector-python==8.0.5`
   - Unidecode library for Python: Run `python3 -m pip install unidecode`

2. Download the source code to your local computer.

3. Navigate to the root directory of the project in your terminal or command prompt.

4. Launch the program by running `python3 ./Program/menu.py` from the terminal or command prompt.

5. The main menu will guide you through the following options:
   - **View a CSV File**: To view match data from CSV files.
   - **Clean Non-ASCII Characters from a CSV File**: To clean up data in CSV files.
   - **Extract or Update Columns in a CSV File**: To manipulate data columns in CSV files.
   - **Split Columns in a CSV File**: To split data into different columns in CSV files.
   - **Connect to MySQL**: To establish a connection with the MySQL database.
   - **Implement Database (Q3 Part 2)**: To create the database and tables using SQL scripts.
   - **Query Database (Q3 Part 3)**: To run queries on the database.
   - **Load Advanced Concepts (Q3 Part 4)**: To explore advanced database features like stored procedures, views, and indexes.
   - **View/Update Database (Q3 Part 5)**: To view and update the database through the Python interface.
   - **Execute Advanced Concepts (Q3 Part 4)**: To execute advanced database concepts programmatically.
   - **Exit Program**: To close the application.

6. Follow the on-screen prompts to perform the desired operations.

7. To exit the program, choose the 'Exit Program' option from the main menu.

Please note that you must connect to the MySQL database through the menu option before attempting to create tables, run queries, or load advanced concepts.

For more detailed information about the program and its features, refer to the **README.md** file in the repository.

## Reflection

The documentation includes a reflection on the design and implementation decisions, challenges faced, and suggestions for improvement based on modern database concepts.
