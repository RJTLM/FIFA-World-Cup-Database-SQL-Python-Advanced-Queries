"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: executeConcepts.py
Purpose: Q3 Part 4
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""

from mysql.connector import Error

# Reference: W3Schools Python MySQL Tutorial (for reading SQL file and executing commands in Python)
def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Reference: "DS Sem2 2023 Lecture Slides" (for executing SQL commands and handling database operations)
def execute_concept(cursor, file_path):
    command = read_sql_file(file_path)
    try:
        print(f"Executing concept:\n{command}")
        cursor.execute(command)
        if cursor.with_rows:  # Check if there are rows to fetch
            results = cursor.fetchall()
            for row in results:
                print(row)
        print("Concept executed successfully.")
    except Error as e:
        # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
        print(f"Error occurred: {e}")
        print(f"Failed concept: {command}")

def execute_concepts(cursor):
    # Reference: "DS Sem2 2023 Lecture Slides" (for understanding of stored procedures and views in databases)
    commands = {
        "1": "./Program/Concepts/callGetTotalMatchesByTeam.sql",
        "2": "./Program/Concepts/callGetAverageAttendanceByYear.sql",
        "3": "./Program/Concepts/selectViewTopScorers.sql",
        "4": "./Program/Concepts/selectViewMatchAttendanceSummary.sql",
        "5": "./Program/Concepts/explainIdxTeamName.sql",
        "6": "./Program/Concepts/explainIdxDateAttendance.sql"
    }

    while True:
        show_menu()
        choice = input("Please enter your choice: ")

        if choice == "0":
            print("Returning to previous menu.")
            break
        elif choice in commands:
            execute_concept(cursor, commands[choice])
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

def show_menu():
    print("\nExecute Concepts")
    print("1: Execute Stored Procedure - GetTotalMatchesByTeam")
    print("2: Execute Stored Procedure - GetAverageAttendanceByYear")
    print("3: Execute View - ViewTopScorers")
    print("4: Execute View - ViewMatchAttendanceSummary")
    print("5: Explain Index - idx_teamname")
    print("6: Explain Index - idx_date_attendance")
    print("0: Return to Main Menu")
