# DSFinalAssignment

## Introduction

This repository contains the implementation of a database system designed to store and query data related to the FIFA Women's World Cup. The project is structured to demonstrate the application of advanced SQL features, such as stored procedures and triggers, and includes a programming language interface to connect to the database.

## Repository Structure

The repository is organized into several directories, each containing SQL scripts for different aspects of the database system:

- `Program/Concepts/`: Contains SQL scripts for database concepts like stored procedures, views, and indexes.
- `Program/Queries/`: Includes SQL scripts for basic and advanced queries.
- `Program/Tables/CreateTables/`: Contains SQL scripts for creating the database, tables, and setting up relationships.

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
