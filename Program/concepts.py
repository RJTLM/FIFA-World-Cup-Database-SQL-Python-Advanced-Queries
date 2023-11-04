import mysql.connector
from mysql.connector import Error

def execute_sql_from_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    commands = sql_script.split(';')[:-1]  # Split by ';' and remove last empty command
    for command in commands:
        try:
            if 'DELIMITER' not in command:
                cursor.execute(command)
            else:
                delimiter_commands = command.split('$$')  # Split by '$$'
                for delimiter_command in delimiter_commands:
                    if delimiter_command.strip() != '':
                        cursor.execute(delimiter_command.strip())
        except Error as e:
            print(f"Error occurred: {e}")

def main():
    # Assuming the user is already connected to the database
    # Replace 'your_database' with the actual database name
    connection = mysql.connector.connect(
        host='localhost',
        database='your_database',
        user='your_username',
        password='your_password'
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        
        # Path to the SQL file
        sql_file_path = './Program/Concepts/advancedConcepts.sql'
        execute_sql_from_file(cursor, sql_file_path)
        
        # Commit changes
        connection.commit()
        
        print("Advanced concepts have been implemented.")
        
        # The user does not need to disconnect when finished, as per the instructions
        # However, we should still clean up the cursor
        cursor.close()
    else:
        print("Failed to connect to the database.")

if __name__ == "__main__":
    main()
