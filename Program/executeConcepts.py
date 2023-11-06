# executeConcepts.py
from mysql.connector import Error

def execute_concept(cursor, command):
    try:
        print(f"Executing concept:\n{command}")
        cursor.execute(command)
        # Fetch and print results if there are any
        results = cursor.fetchall()
        for row in results:
            print(row)
        print("Concept executed successfully.")
    except Error as e:
        print(f"Error occurred: {e}")
        print(f"Failed concept: {command}")

def execute_concepts(cursor, commands):
    while True:
        show_menu()
        choice = input("Please enter your choice: ")

        if choice == "0":
            print("Returning to previous menu.")
            break
        elif choice in commands:
            execute_concept(cursor, commands[choice])
        else:
            print("Invalid choice. Please enter a number between 0 and 6.")

def show_menu():
    print("\nExecute Concepts")
    print("1: Stored Procedure - GetTotalMatchesByTeam")
    print("2: Stored Procedure - GetAverageAttendanceByYear")
    print("3: View - ViewTopScorers")
    print("4: View - ViewMatchAttendanceSummary")
    print("5: Index - idx_teamname")
    print("6: Index - idx_date_attendance")
    print("0: Return to previous menu")
