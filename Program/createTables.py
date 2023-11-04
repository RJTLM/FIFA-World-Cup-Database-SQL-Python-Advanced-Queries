# createTables.py
import os
import mysql.connector
from insertData import insert_data

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
    
    print("Database successfully created: fifa_womens_world_cup_21171466.")

def use_database(cursor):
    # SQL file to execute for using the database
    sql_file = 'useDatabase.sql'
    
    # Base directory for SQL files
    base_dir = './Program/Tables/CreateTables/'
    
    file_path = os.path.join(base_dir, sql_file)
    execute_sql_file(cursor, file_path)
    
    print("Database successfully changed to: fifa_womens_world_cup_21171466.")

def create_tables(cursor):
    # List of SQL files to execute for creating tables
    sql_files = [
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
    
    print("\nTables successfully created.")

def reset(cursor):
    # SQL file to execute for deleting the database to 'reset'
    sql_file = 'deleteDatabase.sql'
    
    # Base directory for SQL files
    base_dir = './Program/Tables/CreateTables/'
    
    file_path = os.path.join(base_dir, sql_file)
    execute_sql_file(cursor, file_path)
    
    print("Database and data successfully deleted: fifa_womens_world_cup_21171466.")


def main(cursor, db_connection):
    while True:
        print("\nDatabase and Tables Setup")
        print("1: Create Database")
        print("2: Use Database")
        print("3: Create Tables")
        print("4: Insert Initial Data into Tables")
        print("5: Reset (WARNING: This deletes the database and all its data)")
        print("0: Return to Main Menu")
        choice = input().strip()
        
        if choice == "1":
            create_database(cursor)
        elif choice == "2":
            use_database(cursor)
        elif choice == "3":
            create_tables(cursor)
        elif choice == "4":
            insert_data(cursor, db_connection)
        elif choice == "5":
            reset(cursor)
        elif choice == "0":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
   