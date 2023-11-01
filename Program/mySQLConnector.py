import mysql.connector
import getpass

def main():
    # Database configuration
    db_config = {
        'host': 'localhost',
        'user': input("Enter your MySQL username: "),
        'password': getpass.getpass("Enter your MySQL password: "),
        'database': 'fifa_womens_world_cup_21171466'
    }

    # Establish a database connection
    db_connection = mysql.connector.connect(**db_config)
    cursor = db_connection.cursor()

    print("Connection established!")
    return cursor, db_connection
