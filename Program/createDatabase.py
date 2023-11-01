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
            # If the command is a source command, read the file and execute its contents
            if command.lower().startswith("source"):
                file_name = command.split()[1].strip(';')
                # Construct the correct path for the sourced file
                new_file_path = os.path.abspath(os.path.join(os.path.dirname(file_path), '..', file_name))
                execute_sql_file(cursor, new_file_path)
            else:
                try:
                    cursor.execute(command)
                    print(f"Executed: {command}")
                except Exception as e:
                    print(f"Failed to execute: {command}")
                    print(f"Error: {str(e)}")

def create_database_and_tables(cursor):
    # Path to your commands.sql file
    sql_file_path = './Program/Tables/commands.sql'
    
    # Execute the SQL commands from the file
    execute_sql_file(cursor, sql_file_path)
    print("Database and tables successfully created.")
