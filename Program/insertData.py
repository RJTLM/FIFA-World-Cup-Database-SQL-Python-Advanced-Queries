# insertData.py
import csv
from mysql.connector import Error

# Function to insert data into the Team, Player, Manager, Referee, Event, FootballMatch, Plays, and Manages tables
def insert_data(cursor, db_connection):
    all_insertions_successful = True # Initialise the variable at the start of the function
    try:
        # Delete existing data in the Event table
        cursor.execute("DELETE FROM Event")
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
        db_connection.commit()
        print("Data successfully inserted into the Event table.")
    except Error as e:
        print(f"Error inserting into Event: {e}")
        all_insertions_successful = False

    try:
        # Delete existing data in the FootballMatch table
        cursor.execute("DELETE FROM FootballMatch")
        # Delete existing data in the Team table
        cursor.execute("DELETE FROM Team")
        # Delete existing data in the Player table
        cursor.execute("DELETE FROM Player")
        # Delete existing data in the Manager table
        cursor.execute("DELETE FROM Manager")
        # Delete existing data in the Referee table
        cursor.execute("DELETE FROM Referee")
        # Delete existing data in the Plays table
        cursor.execute("DELETE FROM Plays")
        # Delete existing data in the Manages table
        cursor.execute("DELETE FROM Manages")
        # Insert data into the FootballMatch, Team, Player, Manager, Referee, Plays, and Manages tables from bigDataCleaned1.csv
        with open('./Program/bigDataCleaned1.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  # Skip the header row
            for row in csvreader:
                # Insert Teams with IGNORE to avoid duplicates
                team_query = "INSERT IGNORE INTO Team (TeamName) VALUES (%s)"
                cursor.execute(team_query, (row[1],))  # home_team
                cursor.execute(team_query, (row[2],))  # away_team

                # Insert Players (Captains) with IGNORE to avoid duplicates
                player_query = "INSERT IGNORE INTO Player (PlayerName, isCaptain) VALUES (%s, TRUE)"
                cursor.execute(player_query, (row[8],))  # home_captain
                cursor.execute(player_query, (row[10],))  # away_captain

                # Insert Managers with IGNORE to avoid duplicates
                manager_query = "INSERT IGNORE INTO Manager (ManagerName) VALUES (%s)"
                cursor.execute(manager_query, (row[7],))  # home_manager
                cursor.execute(manager_query, (row[9],))  # away_manager

                # Insert Referee with IGNORE to avoid duplicates
                referee_query = "INSERT IGNORE INTO Referee (RefereeName) VALUES (%s)"
                cursor.execute(referee_query, (row[15],))  # Referee

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

                # Insert Plays and Manages with checks for existing data
                plays_query = "INSERT IGNORE INTO Plays (MatchID, TeamName) VALUES (%s, %s)"
                manages_query = "INSERT IGNORE INTO Manages (MatchID, ManagerName) VALUES (%s, %s)"
                try:
                    # Before inserting, ensure the TeamName and ManagerName exist in their respective tables
                    # If not, you should insert them first or handle the error accordingly
                    cursor.execute(plays_query, (row[0], row[1])) # MatchID
                    cursor.execute(plays_query, (row[0], row[2])) #TeamName
                    cursor.execute(manages_query, (row[0], row[7]))  # home_manager
                    cursor.execute(manages_query, (row[0], row[9]))  # away_manager
                except Error as e:
                    print(f"Error inserting into Plays or Manages: {e}")

        # Commit changes to the database
        db_connection.commit()
        print("Data successfully inserted into the FootballMatch, Team, Player, Manager, Referee, Plays, and Manages tables.")
    except Error as e:
        print(f"Error processing bigDataCleaned1.csv: {e}")
        db_connection.rollback()
        all_insertions_successful = False

    # After all insertions, check if all were successful
    if all_insertions_successful:
        print("All data successfully inserted into tables.")

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
