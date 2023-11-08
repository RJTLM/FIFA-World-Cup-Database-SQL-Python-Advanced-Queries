"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: mySQLConnector.py
Purpose: Q3 Part 5
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""
import mysql.connector
import getpass
import time  # Importing the time module for creating delays in output

def connect_to_db():
    # Database configuration
    # Reference: "DS Sem2 2023 Lecture Slides" (for understanding of database configuration and connection)
    db_config = {
        'host': 'localhost',
        'user': input("\nEnter your MySQL username: "),
        'password': getpass.getpass("Enter your MySQL password: "),
    }

    # Establish a database connection
    # Reference: W3Schools Python MySQL Tutorial (for establishing a connection to MySQL server in Python)
    db_connection = mysql.connector.connect(**db_config)
    cursor = db_connection.cursor()

    print("\nConnection established!")
    time.sleep(1)  # Wait for 1 second
    # Reference: "FOP Sem2 2023 LectureSlides" (for the use of time module and system interaction)
    return cursor, db_connection

def main():
    # The main function that starts the database connection process
    # Reference: "FOP Sem2 2023 LectureSlides" (for the concept of main function and script execution)
    connect_to_db()

if __name__ == "__main__":
    # Reference: "FOP Sem2 2023 LectureSlides" (for understanding of Python's dunder methods and script execution)
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
