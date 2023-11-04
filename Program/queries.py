# queries.py

def execute_query(cursor, query, params=None):
    try:
        cursor.execute(query, params)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print("Error reading data from MySQL table", e)

def load_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.read().split(';')
    return [query.strip() for query in queries if query.strip()]

def run_query(cursor, query, message, params=None):
    try:
        cursor.execute(query, params)
        records = cursor.fetchall()
        if not records:
            print("No data found.")
            return
        print(message)
        for record in records:
            print(record)
    except Exception as e:
        print("Error:", e)

def main(cursor):
    basic_queries = load_queries('./Program/Queries/basicQueries.sql')
    advanced_queries = load_queries('./Program/Queries/advancedQueries.sql')
    
    while True:
        print("\nWhat would you like to know?")
        print("Basic:")
        print(" 1: Find all matches played by a specific team")
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
        print(" 0: Exit")
        
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            team = input("Enter the team name: ")
            run_query(cursor, basic_queries[0], "Matches played by " + team + ":", (team,))
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
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
