# concepts.py
import re
from mysql.connector import Error

def execute_sql_command(cursor, command):
    try:
        print(f"Executing command:\n{command}")  # Print the command before execution
        cursor.execute(command)
        print("Command executed successfully.")
    except Error as e:
        print(f"Error occurred: {e}")
        print(f"Failed command: {command}")  # Print the failed command

def load_stored_procedures(file_path):
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

def load_views(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    # Split the script using a regular expression to handle different SQL statement terminators
    commands = re.split(r';(?=\s*\w)|END;\s*', sql_script)
    # Remove any empty strings and whitespace from the list of commands
    commands = [command.strip() for command in commands if command.strip()]
    return commands

def interactive_execute(cursor, commands):
    while True:
        print("\nWhich SQL concept would you like to execute?")
        print(" 1: Stored Procedure - GetTotalMatchesByTeam")
        print(" 2: Stored Procedure - GetAverageAttendanceByYear")
        print(" 3: View - ViewTopScorers")
        print(" 4: View - ViewMatchAttendanceSummary")
        print(" 5: Index - idx_teamname")
        print(" 6: Index - idx_date_attendance")
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
    # Paths to the SQL files
    stored_procedures_path = './Program/Concepts/storedProcedures.sql'
    stored_procedures1_path = './Program/Concepts/storedProcedures1.sql'
    views_path = './Program/Concepts/views.sql'
    views1_path = './Program/Concepts/views1.sql'
    indexes_path = './Program/Concepts/indexes.sql'
    indexes1_path = './Program/Concepts/indexes1.sql'
    
    # Load commands from stored procedures and indexes
    stored_procedures_commands = load_stored_procedures(stored_procedures_path)
    stored_procedures1_commands = load_stored_procedures(stored_procedures1_path)
    
    # Load commands from views and indexes
    views_commands = load_views(views_path)
    views1_commands = load_views(views1_path)
    indexes_commands = load_stored_procedures(indexes_path)
    indexes1_commands = load_stored_procedures(indexes1_path)
    
    # Combine all commands
    commands = stored_procedures_commands + stored_procedures1_commands + views_commands + views1_commands + indexes_commands + indexes1_commands
    
    interactive_execute(cursor, commands)
    
    # Commit changes
    connection.commit()
    
    print("Advanced concepts have been implemented interactively.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
