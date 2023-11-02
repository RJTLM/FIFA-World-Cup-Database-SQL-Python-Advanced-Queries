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
        for i, (match_date, home_team, away_team, home_score, away_score) in enumerate(records, start=1):
            formatted_date = match_date.strftime("%d %b %Y")
            print(f"Semi-final {i} was played on {formatted_date} by {home_team} ({home_score}) and {away_team} ({away_score}).")
    except Exception as e:
        print("Error:", e)


def main(cursor):
    basic_queries = load_queries('./Program/Queries/basicQueries.sql')
    advanced_queries = load_queries('./Program/Queries/advancedQueries.sql')
    
    while True:
        print("\nWhat would you like to know?")
        print("Basic:")
        print(" 1: Who won the 2023 FIFA Women's World Cup?")
        print(" 2: What dates were the 2023 semi finals played on?")
        print(" 3: Which referee officiated the most matches?")
        print(" 4: What is the average number of matches per event?")
        print(" 5: List all players who are captains.")
        print("Advanced:")
        print(" 6: Which team has participated in the most matches?")
        print(" 7: Which manager managed teams in the most number of different events?")
        print(" 8: List all teams that have never won an event.")
        print(" 9: Which venue hosted the most matches?")
        print("10: Find the top scorer of the event with the highest average attendance.")
        print(" 0: Return to Main Menu")
        
        choice = input("Please enter your choice: ")
        
        if choice == "1":
            run_query(cursor, basic_queries[0], "The winner of the 2023 FIFA Women's World Cup:")
        elif choice == "2":
            run_query(cursor, basic_queries[1], "What dates were the 2023 semi finals played on:")
        elif choice == "3":
            run_query(cursor, basic_queries[2], "Referee who officiated the most matches:")
        elif choice == "4":
            run_query(cursor, basic_queries[3], "Average number of matches per event:")
        elif choice == "5":
            run_query(cursor, basic_queries[4], "Players who are captains:")
        elif choice == "6":
            run_query(cursor, advanced_queries[0], "Team that has participated in the most matches:")
        elif choice == "7":
            run_query(cursor, advanced_queries[1], "Manager who managed teams in the most number of different events:")
        elif choice == "8":
            run_query(cursor, advanced_queries[2], "Teams that have never won an event:")
        elif choice == "9":
            run_query(cursor, advanced_queries[3], "Venue that hosted the most matches:")
        elif choice == "10":
            run_query(cursor, advanced_queries[4], "Top scorer of the event with the highest average attendance:")
        elif choice == "0":
            print("Returning to the main menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 10.")
