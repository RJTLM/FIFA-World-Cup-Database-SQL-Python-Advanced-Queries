# updateDatabase.py

def insert_data(cursor, db_connection):
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
        print("Error inserting data:", str(e))

def update_data(cursor, db_connection):
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
        print("Error updating data:", str(e))

def delete_data(cursor, db_connection):
    print("\nDelete Data")
    table_name = input("Enter the table name: ")
    where_clause = input("Enter the WHERE clause (e.g., CoachName = 'Peter Parker', CoachName = 'MJ'): ")
    
    sql = f"DELETE FROM {table_name} WHERE {where_clause}"
    try:
        cursor.execute(sql)
        db_connection.commit()
        print("Data deleted successfully.")
    except Exception as e:
        print("Error deleting data:", str(e))

def show_menu():
    print("\nWhat would you like to do?")
    print("1. Insert data")
    print("2. Update data")
    print("3. Delete data")
    print("0. Return to Main Menu")
    choice = input().strip()
    return choice

def main(cursor, db_connection):
    while True:
        choice = show_menu()
        if choice == "1":
            insert_data(cursor, db_connection)
        elif choice == "2":
            update_data(cursor, db_connection)
        elif choice == "3":
            delete_data(cursor, db_connection)
        elif choice == "0":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
