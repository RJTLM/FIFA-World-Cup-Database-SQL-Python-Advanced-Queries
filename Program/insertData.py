# insertData.py
import csv

# Function to insert data into the Team, Player, Manager, Referee, Event, FootballMatch, Plays, and Manages tables
def insert_data(cursor, db_connection):
    # Insert data into the Event table from littleDataCleaned.csv
    with open('./Program/littleDataCleaned.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            event_query = """
            INSERT INTO Event (EventID, EventYear, EventHost, NoTeams, Champion, RunnerUp, TopScorer, EventAttendance, EventAttendanceAvg, NoMatches)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(event_query, tuple(row))

    # Insert data into the FootballMatch, Team, Player, Manager, Referee, Plays, and Manages tables from bigDataCleaned1.csv
    with open('./Program/bigDataCleaned1.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            # Insert Teams, Players, Managers, and Referees with IGNORE to avoid duplicates
            insert_ignore_queries = {
                "Team": "INSERT IGNORE INTO Team (TeamName) VALUES (%s)",
                "Player": "INSERT IGNORE INTO Player (PlayerName) VALUES (%s)",
                "Manager": "INSERT IGNORE INTO Manager (ManagerName) VALUES (%s)",
                "Referee": "INSERT IGNORE INTO Referee (RefereeName) VALUES (%s)"
            }
            for key in insert_ignore_queries:
                cursor.execute(insert_ignore_queries[key], (row[1],))
                cursor.execute(insert_ignore_queries[key], (row[2],))

            # Insert FootballMatch
            match_query = """
            INSERT INTO FootballMatch (MatchID, home_score, away_score, home_penalty, away_penalty, Attendance, Venue, Round, MatchDate, RefereeName, Notes, MatchHost, EventID)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            match_data = (row[0], row[3], row[5], row[4] or None, row[6] or None, row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17])
            cursor.execute(match_query, match_data)

            # Insert Plays and Manages
            plays_query = "INSERT INTO Plays (MatchID, TeamName) VALUES (%s, %s)"
            manages_query = "INSERT INTO Manages (MatchID, ManagerName) VALUES (%s, %s)"
            cursor.execute(plays_query, (row[0], row[1]))
            cursor.execute(plays_query, (row[0], row[2]))
            cursor.execute(manages_query, (row[0], row[6]))
            cursor.execute(manages_query, (row[0], row[8]))

    # Commit changes to the database
    db_connection.commit()

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
# Reference: https://www.w3schools.com/python/python_mysql_insert.asp (for understanding how to insert data into MySQL using Python)
