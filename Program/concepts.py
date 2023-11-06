# concepts.py
from mysql.connector import Error

def execute_sql_command(cursor, command):
    try:
        print(f"Executing command:\n{command}")  # Print the command before execution
        cursor.execute(command)
        print("Command executed successfully.")
    except Error as e:
        print(f"Error occurred: {e}")
        print(f"Failed command: {command}")  # Print the failed command

def load_sql_commands(file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    commands = sql_script.split(';')  # Split by ';'
    return [command.strip() for command in commands if command.strip()]

def interactive_execute(cursor, commands):
    while True:
        print("\nWhich SQL concept would you like to implement?")
        for i, command in enumerate(commands, 1):
            print(f" {i}: {command.split('\n', 1)[0]}")  # Show the first line of each command
        print(" 0: Exit")

        choice = input("Please enter your choice: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == 0:
                print("Exiting the program.")
                break
            elif 1 <= choice <= len(commands):
                execute_sql_command(cursor, commands[choice - 1] + ';')  # Re-add the final semicolon
            else:
                print("Invalid choice. Please enter a number from the list.")
        else:
            print("Please enter a valid number.")

def main(cursor, connection):
    # Path to the SQL file
    sql_file_path = 'advancedConcepts.sql'
    commands = load_sql_commands(sql_file_path)
    
    interactive_execute(cursor, commands)
    
    # Commit changes
    connection.commit()
    
    print("Advanced concepts have been implemented interactively.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
