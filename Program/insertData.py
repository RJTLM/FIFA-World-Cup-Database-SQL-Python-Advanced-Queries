import csv
import re

def insert_into_team(cursor, db_connection, data):
    if not data:
        print("No data to insert into Team table.")
        return
    
    unique_team_names = set(data)
    print("Inserting data into Team table...")
    sql = "INSERT IGNORE INTO Team (TeamName) VALUES (%s)"
    cursor.executemany(sql, [(team_name,) for team_name in unique_team_names])
    db_connection.commit()
    print("Team table data insertion complete. {} rows processed.".format(len(unique_team_names)))

def insert_into_player(cursor, db_connection, data):
    if not data:
        print("No data to insert into Player table.")
        return
    
    unique_player_names = set(data)
    print("Inserting data into Player table...")
    sql = "INSERT IGNORE INTO Player (PlayerName) VALUES (%s)"
    cursor.executemany(sql, [(player_name,) for player_name in unique_player_names])
    db_connection.commit()
    print("Player table data insertion complete. {} rows processed.".format(len(unique_player_names)))

def insert_into_manager(cursor, db_connection, data):
    if not data:
        print("No data to insert into Manager table.")
        return
    
    unique_manager_names = set(data)
    print("Inserting data into Manager table...")
    sql = "INSERT IGNORE INTO Manager (ManagerName) VALUES (%s)"
    cursor.executemany(sql, [(manager_name,) for manager_name in unique_manager_names])
    db_connection.commit()
    print("Manager table data insertion complete. {} rows processed.".format(len(unique_manager_names)))

def insert_into_captain(cursor, db_connection, data):
    if not data:
        print("No data to insert into Captain table.")
        return
    
    unique_captain_names = set(data)
    print("Inserting data into Captain table...")
    sql = "INSERT IGNORE INTO Captain (CaptainName) VALUES (%s)"
    cursor.executemany(sql, [(captain_name,) for captain_name in unique_captain_names])
    db_connection.commit()
    print("Captain table data insertion complete. {} rows processed.".format(len(unique_captain_names)))

def insert_into_referee(cursor, db_connection, data):
    if not data:
        print("No data to insert into Referee table.")
        return
    
    unique_referee_names = set(data)
    print("Inserting data into Referee table...")
    sql = "INSERT IGNORE INTO Referee (RefereeName) VALUES (%s)"
    cursor.executemany(sql, [(referee_name,) for referee_name in unique_referee_names])
    db_connection.commit()
    print("Referee table data insertion complete. {} rows processed.".format(len(unique_referee_names)))

def insert_into_event(cursor, db_connection, data):
    if not data:
        print("No data to insert into Event table.")
        return
    
    print("Inserting data into Event table...")
    sql = "INSERT IGNORE INTO Event (EventID, EventYear, EventHost, NoTeams, Champion, RunnerUp, TopScorer, EventAttendance, EventAttendanceAvg, NoMatches) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    cursor.executemany(sql, data)
    db_connection.commit()
    print("Event table data insertion complete. {} rows processed.".format(len(data)))

def extract_data_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        team_data = []
        player_data = []
        manager_data = []
        captain_data = []
        referee_data = []
        event_data = []
        for row in csv_reader:
            # Add your logic to extract and append data to the lists above
            # Example:
            team_data.append(row['TeamName'])
            player_data.append(row['PlayerName'])
            manager_data.append(row['ManagerName'])
            captain_data.append(row['CaptainName'])
            referee_data.append(row['RefereeName'])
            event_data.append((row['EventID'], row['EventYear'], row['EventHost'], row['NoTeams'], row['Champion'], row['RunnerUp'], row['TopScorer'], row['EventAttendance'], row['EventAttendanceAvg'], row['NoMatches']))
            
    return team_data, player_data, manager_data, captain_data, referee_data, event_data

def insert_data(cursor, db_connection):
    print("Starting data insertion process...")
    
    # File path to your CSV file
    csv_file_path = './Program/bigDataCleaned.csv'
    
    try:
        team_data, player_data, manager_data, captain_data, referee_data, event_data = extract_data_from_csv(csv_file_path)
        
        # Insert data into tables
        insert_into_team(cursor, db_connection, team_data)
        insert_into_player(cursor, db_connection, player_data)
        insert_into_manager(cursor, db_connection, manager_data)
        insert_into_captain(cursor, db_connection, captain_data)
        insert_into_referee(cursor, db_connection, referee_data)
        insert_into_event(cursor, db_connection, event_data)
        
        print("Data insertion complete.")
    except Exception as e:
        print("An error occurred during the data insertion process.")
        print("Error: {}".format(str(e)))

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
   