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
        if command.strip() != "":
            # If the command is a source command, read the file and execute its contents
            if command.strip().lower().startswith("source"):
                file_name = command.split()[1].strip(';')
                execute_sql_file(cursor, os.path.join(os.path.dirname(file_path), file_name))
            else:
                cursor.execute(command)
                print(f"Executed: {command}")

def create_database_and_tables(cursor):
    # Path to your commands.sql file
    sql_file_path = './Program/Tables/commands.sql'
    
    # Execute the SQL commands from the file
    execute_sql_file(cursor, sql_file_path)
    print("Database and tables successfully created.")
