import mysql.connector
import getpass
import time  # Importing the time module for creating delays in output

def connect_to_db():
    # Database configuration
    db_config = {
        'host': 'localhost',
        'user': input("\nEnter your MySQL username: "),
        'password': getpass.getpass("Enter your MySQL password: "),
        'database': 'fifa_womens_world_cup_21171466'
    }

    # Establish a database connection
    db_connection = mysql.connector.connect(**db_config)
    cursor = db_connection.cursor()

    print("\nConnection established!")
    time.sleep(1.5)  # Wait for 1.5 seconds
    return cursor, db_connection

def main():
    connect_to_db()

if __name__ == "__main__":
    main()
