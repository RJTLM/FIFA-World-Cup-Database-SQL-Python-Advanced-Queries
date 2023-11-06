# executeConcepts.py
from mysql.connector import Error

def read_sql_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def execute_concept(cursor, file_path):
    command = read_sql_file(file_path)
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

def execute_concepts(cursor):
    commands = {
        "1": "./Program/Concepts/callGetTotalMatchesByTeam.sql",
        "2": "./Program/Concepts/callGetAverageAttendanceByYear.sql",
        "3": "./Program/Concepts/selectViewTopScorers.sql",
        "4": "./Program/Concepts/selectViewMatchAttendanceSummary.sql",
        "5": "./Program/Concepts/explainIdxTeamName.sql",
        "6": "./Program/Concepts/explainIdxDateAttendance.sql"
    }

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
    print("1: Execute Stored Procedure - GetTotalMatchesByTeam")
    print("2: Execute Stored Procedure - GetAverageAttendanceByYear")
    print("3: Execute View - ViewTopScorers")
    print("4: Execute View - ViewMatchAttendanceSummary")
    print("5: Explain Index - idx_teamname")
    print("6: Explain Index - idx_date_attendance")
    print("0: Return to Main Menu")
