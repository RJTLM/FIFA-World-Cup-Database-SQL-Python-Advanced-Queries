import mysql.connector
import getpass

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
    return cursor, db_connection

def main():
    connect_to_db()

if __name__ == "__main__":
    main()
