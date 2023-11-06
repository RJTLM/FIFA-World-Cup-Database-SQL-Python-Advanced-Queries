# concepts.py
from mysql.connector import Error

def execute_sql_from_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    commands = sql_script.split(';')  # Split by ';'
    buffer = []
    for command in commands:
        if command.strip() != '':
            # Check for the start of a stored procedure or trigger
            if 'create procedure' in command.lower() or 'create trigger' in command.lower():
                buffer = [command]
            # Check for the end of a stored procedure or trigger
            elif buffer and 'end' in command.lower():
                buffer.append(command)
                full_command = ';'.join(buffer)  # Re-add the final semicolon
                try:
                    cursor.execute(full_command)
                    buffer = []  # Reset the buffer
                except Error as e:
                    print(f"Error occurred: {e}")
            else:
                if buffer:
                    buffer.append(command)
                else:
                    try:
                        cursor.execute(command + ';')  # Ensure each command ends with a semicolon
                    except Error as e:
                        print(f"Error occurred: {e}")

def main(cursor, connection):
    # Path to the SQL file
    sql_file_path = './Program/Concepts/advancedConcepts.sql'
    execute_sql_from_file(cursor, sql_file_path)
    
    # Commit changes
    connection.commit()
    
    print("Advanced concepts have been implemented.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
