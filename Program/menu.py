# menu.py
import time  # Importing the time module for creating delays in output

# Global variables to store the database connection and cursor
db_connection = None
cursor = None

def show_menu(first_time):
    if first_time:
        print("\nWelcome to the FIFA WWC Data Processing Program!")
        print("What would you like to do?")
    else:
        print("\nWelcome Back to the Main Menu!")
        time.sleep(0.75)  # Wait for 0.75 seconds
        print("What would you like to do?")
        time.sleep(0.50)  # Wait for 0.50 seconds
    print(" 1: View a CSV File")
    print(" 2: Clean Non-ASCII Characters from a CSV File")
    print(" 3: Extract or Update Columns in a CSV File")
    print(" 4: Split Columns in a CSV File")
    print(" 5: Connect to MySQL")
    print(" 6: Implement Database (Q3 Part 2)")
    print(" 7: Query Database (Q3 Part 3)")
    print(" 8: Load Advanced Concepts (Q3 Part 4)")
    print(" 9: View/Update Database (Q3 Part 5)")
    print(" 10: Execute Advanced Concepts (Q3 Part 4)")
    print(" 0: Exit Program")
    choice = input().strip()  # Using strip to remove any leading or trailing whitespaces
    return choice
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding functions and user interactions in Python)
    # Reference: https://docs.python.org/3/library/stdtypes.html#str.strip (for understanding the strip function)

def main():
    global db_connection, cursor
    first_time = True
    while True:
        choice = show_menu(first_time)
        if first_time:
            first_time = False
        if choice == "1":
            from dataViewer import main as view_csv
            view_csv()
        elif choice == "2":
            from asciiConversion import main as clean_ascii
            clean_ascii()
        elif choice == "3":
            from extractData import main as extract_data
            extract_data()
        elif choice == "4":
            from splitColumn import main as split_columns
            split_columns()
        elif choice == "5":
            from mySQLConnector import connect_to_db
            cursor, db_connection = connect_to_db()
        elif choice == "6":
            if cursor is not None and db_connection is not None:
                from createTables import main as create_db_and_tables
                create_db_and_tables(cursor, db_connection)
            else:
                print("Please connect to the MySQL Database first.")
        elif choice == "7":
            if cursor is not None and db_connection is not None:
                from queries import main as query_database
                query_database(cursor, db_connection)
            else:
                print("Please connect to the MySQL Database first.")
        elif choice == "8":
            if cursor is not None and db_connection is not None:
                from concepts import main as implement_advanced_concepts
                implement_advanced_concepts(cursor, db_connection)
            else:
                print("Please connect to the MySQL Database first.")
        elif choice == "9":
            if cursor is not None and db_connection is not None:
                from updateDatabase import main as update_database
                update_database(cursor, db_connection)
            else:
                print("Please connect to the MySQL Database first.")
        elif choice == "10":
            if cursor is not None:
                from executeConcepts import execute_concepts
                execute_concepts(cursor)
            else:
                print("Please connect to the MySQL Database first.")
        elif choice == "0":
            print("Why do programmers like dark mode?")
            time.sleep(1.5)  # Wait for 1.5 seconds
            print("\nBecause light attracts bugs", end="", flush=True)
            time.sleep(3)  # Wait for 3 seconds
            print(".", end="", flush=True)
            time.sleep(0.75)  # Wait for 0.75 seconds
            print(".", end="", flush=True)
            time.sleep(0.75)  # Wait for 0.75 seconds
            print(".", end="", flush=True)
            time.sleep(0.75)  # Wait for 0.75 seconds
            print(" ", end="", flush=True)
            time.sleep(2)  # Wait for 2 seconds
            print("\n\nAnyway")
            time.sleep(1)  # Wait for 1 second
            print("Goodbye :)")
            if cursor:
                cursor.close()
            if db_connection:
                db_connection.close()
            break
        else:
            print("Invalid option. Please choose a valid option.")
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding control flow and modular programming in Python)
    # Reference: https://docs.python.org/3/library/time.html#time.sleep (for understanding the time.sleep function)

if __name__ == "__main__":
    main()
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding the main function and script execution in Python)
