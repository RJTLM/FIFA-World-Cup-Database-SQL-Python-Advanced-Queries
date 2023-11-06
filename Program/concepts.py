"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: concepts.py
Purpose: Q3 Part 4
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""

import re
from mysql.connector import Error

# Reference: "FOP Sem2 2023 LectureSlides" (for understanding the structure and execution of Python scripts)
# Reference: "DS Sem2 2023 Lecture Slides" (for understanding database concepts and SQL command execution)
# Online Reference: https://www.w3schools.com/python/python_mysql_getstarted.asp (for basic MySQL operations in Python)

def execute_sql_command(cursor, command):
    # Online Reference: https://www.mysqltutorial.org/python-mysql-execute-sql/
    try:
        print(f"Executing command:\n{command}")  # Print the command before execution
        cursor.execute(command, multi=True)
        for result in cursor:
            if result.with_rows:
                print(result.fetchall())
        print("Command executed successfully.")
    except Error as e:
        print(f"Error occurred: {e}")
        print(f"Failed command: {command}")  # Print the failed command

def load_stored_procedures(file_path):
    # Online Reference: https://docs.python.org/3/library/re.html (for regex operations in Python)
    with open(file_path, 'r') as file:
        sql_script = file.read()
    # Use regex to match only the CREATE PROCEDURE and its contents
    commands = re.findall(r'CREATE PROCEDURE.*?END;', sql_script, re.DOTALL)
    return commands

def load_views(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    # Use regex to match only the CREATE VIEW and its contents
    commands = re.findall(r'CREATE VIEW.*?;', sql_script, re.DOTALL)
    return commands

def load_indexes(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    # Use regex to match only the CREATE INDEX and its contents
    commands = re.findall(r'CREATE INDEX.*?;', sql_script, re.DOTALL)
    return commands

def interactive_execute(cursor, commands):
    # Reference: "FOP Sem2 2023 LectureSlides" (for understanding user interaction in Python)
    while True:
        print("\nWhich SQL concept would you like to load?")
        print(" 1: Stored Procedure - GetTotalMatchesByTeam")
        print(" 2: Stored Procedure - GetAverageAttendanceByYear")
        print(" 3: View - ViewTopScorers")
        print(" 4: View - ViewMatchAttendanceSummary")
        print(" 5: Index - idx_teamname")
        print(" 6: Index - idx_date_attendance")
        print(" 0: Return to Main Menu")

        choice = input("Please enter your choice: ")

        if choice in commands:
            execute_sql_command(cursor, commands[choice])  # Execute the selected command
        elif choice == "0":
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 7.")

def main(cursor, connection):
    # Reference: "DS Sem2 2023 Lecture Slides" (for understanding the setup and use of SQL files in database management)
    # Online Reference: https://realpython.com/python-sql-libraries/#mysql (for working with MySQL in Python)
    
    # Paths to the SQL files
    stored_procedures_path = './Program/Concepts/storedProcedures.sql'
    stored_procedures1_path = './Program/Concepts/storedProcedures1.sql'
    views_path = './Program/Concepts/views.sql'
    views1_path = './Program/Concepts/views1.sql'
    indexes_path = './Program/Concepts/indexes.sql'
    indexes1_path = './Program/Concepts/indexes1.sql'
    
    # Load commands from stored procedures
    stored_procedures_commands = load_stored_procedures(stored_procedures_path)
    stored_procedures1_commands = load_stored_procedures(stored_procedures1_path)
    
    # Load commands from views
    views_commands = load_views(views_path)
    views1_commands = load_views(views1_path)
    
    # Load commands from indexes using the new load_indexes function
    indexes_commands = load_indexes(indexes_path)
    indexes1_commands = load_indexes(indexes1_path)
    
    # Combine all commands in the order they appear in the menu
    commands = {
        "1": stored_procedures_commands[0],
        "2": stored_procedures1_commands[0],
        "3": views_commands[0],
        "4": views1_commands[0],
        "5": indexes_commands[0],
        "6": indexes1_commands[0]
    }
    
    interactive_execute(cursor, commands)
    
    # Commit changes
    connection.commit()
    
    print("Advanced concepts have been implemented interactively.")

if __name__ == "__main__":
    # Reference: "FOP Sem2 2023 LectureSlides" (for understanding the __name__ guard in Python scripts)
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
