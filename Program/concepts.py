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
    
    # Split the script into individual statements
    # This regex pattern looks for semicolons that are followed by a line break and a word character (indicating the start of a new statement)
    # It also considers 'END;' as a valid separator for stored procedures and triggers
    commands = re.split(r';(?=\s*\w)|END;\s*', sql_script)
    
    # Remove any empty strings and whitespace from the list of commands
    commands = [command.strip() for command in commands if command.strip()]
    
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
