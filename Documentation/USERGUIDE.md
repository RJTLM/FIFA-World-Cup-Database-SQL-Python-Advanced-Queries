# User Guide for Database Implementation and Usage
## Final Assessment: Database System for FIFA Women's World Cup
### Student Name: Ryan Mackintosh
### Student ID: 21171466
### Lab Group: Thursday 8am

## Introduction

This guide provides step-by-step instructions for implementing and using the MySQL database designed for the FIFA Women's World Cup project. By following these instructions, you should be able to set up the database on a MySQL server and execute the developed queries.

## Step-By-Step Instructions To Run This Program:

1. Ensure you have the necessary software, packages, and libraries installed including:
   - Python 3
   - MySQL Connector for Python: Run `python3 -m pip install mysql-connector-python==8.0.5`
   - Unidecode library for Python: Run `python3 -m pip install unidecode`

2. Download the program files to your local computer.

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

Please note that you must connect to the MySQL database through menu option 5 before attempting to create tables, run queries, or load advanced concepts.

For more detailed information about the program and its features, refer to the **README.md** file in the repository.