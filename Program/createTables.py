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

def create_database_and_tables(cursor):
    # List of SQL files to execute
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
    
    print("Tables successfully created.")
