# concepts.py
from mysql.connector import Error
import re

def execute_sql_command(cursor, command):
    try:
        print(f"Executing command:\n{command}")  # Print the command before execution
        cursor.execute(command)
        print("Command executed successfully.")
    except Error as e:
        print(f"Error occurred: {e}")
        print(f"Failed command: {command}")  # Print the failed command

def load_sql_concepts(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    # Split by 'END;' to handle stored procedures and triggers correctly
    commands = sql_script.split('END;')
    # Add 'END;' back to the commands where it was removed by split
    commands = [command.strip() + 'END;' for command in commands if command.strip()]
    # Remove the last 'END;' that was added to the last command
    if commands[-1].endswith('END;'):
        commands[-1] = commands[-1][:-4].strip()
    return commands

def interactive_execute(cursor, commands):
    while True:
        print("\nWhich SQL concept would you like to execute?")
        print(" 1: Stored Procedure - GetTotalMatchesByTeam")
        print(" 2: Stored Procedure - GetAverageAttendanceByYear")
        print(" 3: Trigger - BeforeInsertFootballMatch")
        print(" 4: Trigger - AfterUpdateEvent")
        print(" 5: View - ViewTopScorers")
        print(" 6: View - ViewMatchAttendanceSummary")
        print(" 7: Index - idx_teamname")
        print(" 8: Index - idx_date_attendance")
        print(" 0: Return to Main Menu")

        choice = input("Please enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print("Returning to the main menu.")
                break
            elif 1 <= choice <= len(commands):
                execute_sql_command(cursor, commands[choice - 1])  # Execute the selected command
            else:
                print("Invalid choice. Please enter a number from the list.")
        else:
            print("Please enter a valid number.")

def main(cursor, connection):
    # Path to the SQL file
    sql_file_path = './Program/Concepts/advancedConcepts.sql'
    commands = load_sql_concepts(sql_file_path)
    
    interactive_execute(cursor, commands)
    
    # Commit changes
    connection.commit()
    
    print("Advanced concepts have been implemented interactively.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
