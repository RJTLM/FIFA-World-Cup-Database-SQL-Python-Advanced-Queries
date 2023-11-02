# queries.py

def execute_query(cursor, query):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        return records
    except Exception as e:
        print("Error reading data from MySQL table", e)

def load_queries(file_path):
    with open(file_path, 'r') as file:
        queries = file.read().split(';')
    return [query.strip() for query in queries if query.strip()]

def run_query(cursor, query, message):
    try:
        cursor.execute(query)
        records = cursor.fetchall()
        if not records:
            print("No data found.")
            return
        print(message)
        # Fetching column headers
        column_headers = [desc[0] for desc in cursor.description]
        print("\t".join(column_headers))
        for record in records:
            print("\t".join(map(str, record)))
    except Exception as e:
        print("Error:", e)


def main(cursor):
    basic_queries = load_queries('./Program/Queries/basicQueries.sql')
    advanced_queries = load_queries('./Program/Queries/advancedQueries.sql')
    
    while True:
        print("\nWhat would you like to know?")
        print("Basic:")
        print(" 1: Find all matches played at a specific venue")
        print(" 2: Retrieve all matches with attendance greater than a specific number")
        print(" 3: Get details of matches played in a specific date range")
        print(" 4: Find all matches where a specific team was the home team and scored more than 2 goals")
        print(" 5: Retrieve all matches with a specific referee and notes not null")
        print("Advanced:")
        print(" 6: Find the total number of matches played by each team")
        print(" 7: Get the average attendance of matches for each venue")
        print(" 8: Find the top scorer of each event")
        print(" 9: Get the total number of goals scored in each round of an event")
        print("10: Find all matches where penalty kicks were taken and the match was hosted in a specific year")
        print(" 0: Return to Main Menu")
        
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            run_query(cursor, basic_queries[0], "Matches played at a specific venue:")
        elif choice == "2":
            run_query(cursor, basic_queries[1], "Matches with attendance greater than a specific number:")
        elif choice == "3":
            run_query(cursor, basic_queries[2], "Matches played in a specific date range:")
        elif choice == "4":
            run_query(cursor, basic_queries[3], "Matches where a specific team was the home team and scored more than 2 goals:")
        elif choice == "5":
            run_query(cursor, basic_queries[4], "Matches with a specific referee and notes not null:")
        elif choice == "6":
            run_query(cursor, advanced_queries[0], "Total number of matches played by each team:")
        elif choice == "7":
            run_query(cursor, advanced_queries[1], "Average attendance of matches for each venue:")
        elif choice == "8":
            run_query(cursor, advanced_queries[2], "Top scorer of each event:")
        elif choice == "9":
            run_query(cursor, advanced_queries[3], "Total number of goals scored in each round of an event:")
        elif choice == "10":
            run_query(cursor, advanced_queries[4], "Matches where penalty kicks were taken and the match was hosted in a specific year:")
        elif choice == "0":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")
