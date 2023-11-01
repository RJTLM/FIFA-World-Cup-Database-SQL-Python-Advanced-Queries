# viewData.py

def view_tables(cursor, db_connection):
    print("\nView Tables")
    try:
        cursor.execute("SHOW TABLES")
        tables = cursor.fetchall()
        if tables:
            print("Tables in the database:")
            for table in tables:
                print(table[0])
        else:
            print("No tables found in the database.")
    except Exception as e:
        print("Error fetching tables:", str(e))

def view_table_columns(cursor, db_connection):
    print("\nView Table Columns")
    table_name = input("Enter the table name: ")
    try:
        cursor.execute(f"DESCRIBE {table_name}")
        columns = cursor.fetchall()
        if columns:
            print(f"Columns in the table {table_name}:")
            for column in columns:
                print(column[0])
        else:
            print(f"No columns found in the table {table_name}.")
    except Exception as e:
        print("Error fetching table columns:", str(e))

def view_table_data(cursor, db_connection):
    print("\nView Table Data")
    table_name = input("Enter the table name: ")
    try:
        cursor.execute(f"SELECT * FROM {table_name}")
        data = cursor.fetchall()
        if data:
            print(f"Data in the table {table_name}:")
            for row in data:
                print(row)
        else:
            print(f"No data found in the table {table_name}.")
    except Exception as e:
        print("Error fetching table data:", str(e))

def show_menu():
    print("\nWhat would you like to do?")
    print("1: View Tables")
    print("2: View Table Columns")
    print("3: View Table Data")
    print("0: Return to Previous Menu")
    choice = input().strip()
    return choice

def main(cursor, db_connection):
    while True:
        choice = show_menu()
        if choice == "1":
            view_tables(cursor, db_connection)
        elif choice == "2":
            view_table_columns(cursor, db_connection)
        elif choice == "3":
            view_table_data(cursor, db_connection)
        elif choice == "0":
            print("Returning to Previous Menu...")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
