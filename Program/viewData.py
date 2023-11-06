"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: viewData.py
Purpose: Q3 Part 5
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""

def view_tables(cursor):
    # Reference: "DS Sem2 2023 Lecture Slides" (for SQL 'SHOW TABLES' command)
    print("\nView Tables")
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
    except Exception as e:
        # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
        print("Error fetching tables:", str(e))

def view_table_columns(cursor):
    # Reference: "DS Sem2 2023 Lecture Slides" (for SQL 'DESCRIBE' command)
    print("\nView Table Columns")
    table_name = input("Enter the table name: ")
    try:
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        if columns:
            print(f"Columns in the table {table_name}:")
            for column in columns:
                print(column[0])
        else:
            print(f"No columns found in the table {table_name}.")
    except Exception as e:
        # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
        print("Error fetching table columns:", str(e))

def view_table_data(cursor):
    # Reference: "DS Sem2 2023 Lecture Slides" (for SQL 'SELECT * FROM' command)
    print("\nView Table Data")
    table_name = input("Enter the table name: ")
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        if data:
            print(f"Data in the table {table_name}:")
            for row in data:
                print(row)
        else:
            print(f"No data found in the table {table_name}.")
    except Exception as e:
        # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
        print("Error fetching table data:", str(e))

if __name__ == "__main__":
    # Reference: W3Schools Python MySQL Tutorial (for the general structure of a Python script interacting with MySQL)
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
