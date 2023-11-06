# concepts.py
from mysql.connector import Error

def execute_sql_from_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
    commands = sql_script.split(';')  # Split by ';'
    for command in commands:
        try:
            if command.strip() != '':
                cursor.execute(command.strip())
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