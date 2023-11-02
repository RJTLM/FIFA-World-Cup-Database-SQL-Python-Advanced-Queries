import os

def execute_sql_file(cursor, file_path):
    """
    Execute SQL commands from a file using the provided cursor.
    """
    with open(file_path, 'r') as file:
        sql_script = file.read()
    
    # Split the script into individual commands based on the semicolon
    commands = sql_script.split(';')
    
    for command in commands:
        command = command.strip()
        if command:
            try:
                cursor.execute(command)
                print(f"Executed: {command}")
            except Exception as e:
                print(f"Failed to execute: {command}")
                print(f"Error: {str(e)}")

def create_database(cursor):
    # SQL file to execute for creating the database
    sql_file = 'createDatabase.sql'
    
    # Base directory for SQL files
    base_dir = './Program/Tables/CreateTables/'
    
    file_path = os.path.join(base_dir, sql_file)
    execute_sql_file(cursor, file_path)
    
    print("Database successfully created.")

def create_tables(cursor):
    # List of SQL files to execute for creating tables
    sql_files = [
        'createBigData.sql',
        'createLittleData.sql',
        'createTablesWithoutFKDep.sql',
        'createTablesWithFKDep.sql',
        'createRelationshipSets.sql'
    ]
    
    # Base directory for SQL files
    base_dir = './Program/Tables/CreateTables/'
    
    # Execute each SQL file in order
    for sql_file in sql_files:
        file_path = os.path.join(base_dir, sql_file)
        execute_sql_file(cursor, file_path)
    
    print("Tables successfully created.")

def main(cursor):
    while True:
        print("\nDatabase and Tables Setup")
        print("1: Create Database")
        print("2: Create Tables")
        print("0: Return to Main Menu")
        choice = input("Choose an option: ").strip()
        
        if choice == "1":
            create_database(cursor)
        elif choice == "2":
            create_tables(cursor)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
   