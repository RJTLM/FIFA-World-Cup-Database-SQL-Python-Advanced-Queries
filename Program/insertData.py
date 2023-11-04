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
            INSERT INTO FootballMatch (MatchID, home_score, away_score, home_penalty, away_penalty, Attendance, Venue, Round, MatchDate, Notes, MatchHost)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            match_data = (
                row[0],  # MatchID
                row[3],  # home_score
                row[5],  # away_score
                row[4] if row[4] != '' else None,  # home_penalty
                row[6] if row[6] != '' else None,  # away_penalty
                row[11],  # Attendance
                row[12],  # Venue
                row[13],  # Round
                row[14],  # MatchDate
                row[16],  # Notes
                row[17],  # MatchHost
            )

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
