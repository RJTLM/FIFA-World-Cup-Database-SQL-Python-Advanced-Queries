"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: queries.py
Purpose: Q3 Part 3
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""

def execute_query(cursor, query, params=None):
    # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
    try:
        cursor.execute(query, params)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print("Error reading data from MySQL table", e)

# Reference: "DS Sem2 2023 Lecture Slides" (for understanding SQL file handling and execution)
def load_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.read().split(';')
    return [query.strip() for query in queries if query.strip()]

def run_query(cursor, query, message, params=None):
    # Reference: "FOP Sem2 2023 LectureSlides" (for exception handling in Python)
    # Reference: "DS Sem2 2023 Lecture Slides" (for SQL query execution and result fetching)
    try:
        cursor.execute(query, params)
        records = cursor.fetchall()
        if not records:
            print("No data found.")
            return
        print(message)
        
        # Fetch column headers
        headers = [i[0] for i in cursor.description]
        # Print column headers
        print('\t'.join(headers))
        
        # Print records with headers
        for record in records:
            print('\t'.join(str(field) for field in record))
    except Exception as e:
        print("Error:", e)

def main(cursor):
    basic_queries = load_queries('./Program/Queries/basicQueries.sql')
    advanced_queries = load_queries('./Program/Queries/advancedQueries.sql')
    
    while True:
        print("\nWhat would you like to know?")
        print("Basic:")
        print(" 1: Find all matches played by Sweden")
        print(" 2: Retrieve all matches with attendance greater than 50,000")
        print(" 3: Get details of matches played in August 2023")
        print(" 4: Find all matches where the home team scored more than 2 goals")
        print(" 5: Retrieve all matches refereed by 'Tori Penso'")
        print("Advanced:")
        print(" 6: Find the total number of matches played by each team")
        print(" 7: Get the average attendance of matches for each venue")
        print(" 8: Find the top scorer of each event")
        print(" 9: Get the total number of goals scored in each round of the 2023 event")
        print("10: Find all matches where penalty kicks were taken in the 2023 event")
        print(" 0: Return to Main Menu")
        
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            run_query(cursor, basic_queries[0], "Matches played by Sweden:")
        elif choice == "2":
            run_query(cursor, basic_queries[1], "Matches with attendance greater than 50,000:")
        elif choice == "3":
            run_query(cursor, basic_queries[2], "Matches played in August 2023:")
        elif choice == "4":
            run_query(cursor, basic_queries[3], "Matches where the home team scored more than 2 goals:")
        elif choice == "5":
            run_query(cursor, basic_queries[4], "Matches refereed by 'Tori Penso':")
        elif choice == "6":
            run_query(cursor, advanced_queries[0], "Total number of matches played by each team:")
        elif choice == "7":
            run_query(cursor, advanced_queries[1], "Average attendance of matches for each venue:")
        elif choice == "8":
            run_query(cursor, advanced_queries[2], "Top scorer of each event:")
        elif choice == "9":
            run_query(cursor, advanced_queries[3], "Total number of goals scored in each round of the 2023 event:")
        elif choice == "10":
            run_query(cursor, advanced_queries[4], "Matches where penalty kicks were taken in the 2023 event:")
        elif choice == "0":
            print("Returning to Main Menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")



"""
# Reference: W3Schools Python MySQL Tutorial (for pretty table formatting and advanced database operations)
If prettytable is installed:
from prettytable import PrettyTable # pip install prettytable

def run_query(cursor, query, message, params=None):
    try:
        cursor.execute(query, params)
        records = cursor.fetchall()
        if not records:
            print("No data found.")
            return
        print(message)
        
        # Fetch column headers
        headers = [i[0] for i in cursor.description]
        
        # Create a PrettyTable and add the headers
        table = PrettyTable()
        table.field_names = headers
        
        # Add rows to the table
        for record in records:
            table.add_row(record)
        
        # Print the table
        print(table)
    except Exception as e:
        print("Error:", e)"""