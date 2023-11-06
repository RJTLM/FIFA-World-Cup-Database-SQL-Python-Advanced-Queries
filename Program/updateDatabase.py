"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: updateDatabase.py
Purpose: Q3 Part 5
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""

def view_data(cursor, db_connection):
    # Reference: "FOP Sem2 2023 LectureSlides" (for modular programming and function definition)
    from viewData import main as view_data_main
    view_data_main(cursor, db_connection)

def insert_data(cursor, db_connection):
    # Reference: "DS Sem2 2023 Lecture Slides" (for SQL INSERT operation)
    # Reference: W3Schools Python MySQL Tutorial (for executing SQL commands in Python)
    print("\nInsert Data")
    table_name = input("Enter the table name: ")
    columns = input("Enter the columns (comma-separated): ")
    values = input("Enter the values (comma-separated): ")
    
    sql = f"INSERT INTO {table_name} ({columns}) VALUES ({values})"
    try:
        cursor.execute(sql)
        db_connection.commit()
        print("Data inserted successfully.")
    except Exception as e:
        # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
        print("Error inserting data:", str(e))

def update_data(cursor, db_connection):
    # Reference: "DS Sem2 2023 Lecture Slides" (for SQL UPDATE operation)
    # Reference: W3Schools Python MySQL Tutorial (for executing SQL commands in Python)
    print("\nUpdate Data")
    table_name = input("Enter the table name: ")
    set_clause = input("Enter the SET clause (e.g., CoachName = 'Peter Griffin', CoachName = 'Lois Griffin'): ")
    where_clause = input("Enter the WHERE clause (e.g., CoachName = 'Peter Parker', CoachName = 'MJ'): ")
    
    sql = f"UPDATE {table_name} SET {set_clause} WHERE {where_clause}"
    try:
        cursor.execute(sql)
        db_connection.commit()
        print("Data updated successfully.")
    except Exception as e:
        # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
        print("Error updating data:", str(e))

def delete_data(cursor, db_connection):
    # Reference: "DS Sem2 2023 Lecture Slides" (for SQL DELETE operation)
    # Reference: W3Schools Python MySQL Tutorial (for executing SQL commands in Python)
    print("\nDelete Data")
    table_name = input("Enter the table name: ")
    where_clause = input("Enter the WHERE clause (e.g., CoachName = 'Peter Parker', CoachName = 'MJ'): ")
    
    sql = f"DELETE FROM {table_name} WHERE {where_clause}"
    try:
        cursor.execute(sql)
        db_connection.commit()
        print("Data deleted successfully.")
    except Exception as e:
        # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
        print("Error deleting data:", str(e))

def show_menu():
    # Reference: "FOP Sem2 2023 LectureSlides" (for user input and control structures)
    print("\nWhat would you like to do?")
    print("1: View Data")
    print("2: Insert Data")
    print("3: Update Data")
    print("4: Delete Data")
    print("0: Return to Main Menu")
    choice = input().strip()
    return choice

def main(cursor, db_connection):
    # Reference: "FOP Sem2 2023 LectureSlides" (for control structures and program flow)
    while True:
        choice = show_menu()
        if choice == "1":
            view_data(cursor, db_connection)
        elif choice == "2":
            insert_data(cursor, db_connection)
        elif choice == "3":
            update_data(cursor, db_connection)
        elif choice == "4":
            delete_data(cursor, db_connection)
        elif choice == "0":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    # Reference: "FOP Sem2 2023 LectureSlides" (for Python script entry point)
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
