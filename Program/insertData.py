# insertData.py
import csv

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
    
    print("Inserting data into Player table...")
    sql = "INSERT IGNORE INTO Player (PlayerName, isCaptain) VALUES (%s, %s)"
    cursor.executemany(sql, data)
    db_connection.commit()
    print("Player table data insertion complete. {} rows processed.".format(len(data)))

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

def insert_into_football_match(cursor, db_connection, data):
    if not data:
        print("No data to insert into FootballMatch table.")
        return
    
    print("Inserting data into FootballMatch table...")
    sql = """
    INSERT IGNORE INTO FootballMatch 
    (MatchID, home_score, away_score, home_penalty, away_penalty, Attendance, Venue, Round, MatchDate, Notes, MatchHost, EventID, RefereeName) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.executemany(sql, data)
    db_connection.commit()
    print("FootballMatch table data insertion complete. {} rows processed.".format(len(data)))

def insert_into_plays(cursor, db_connection, data):
    if not data:
        print("No data to insert into Plays table.")
        return
    
    print("Inserting data into Plays table...")
    sql = "INSERT IGNORE INTO Plays (MatchID, TeamName) VALUES (%s, %s)"
    cursor.executemany(sql, data)
    db_connection.commit()
    print("Plays table data insertion complete. {} rows processed.".format(len(data)))

def insert_into_manages(cursor, db_connection, data):
    if not data:
        print("No data to insert into Manages table.")
        return
    
    print("Inserting data into Manages table...")
    sql = "INSERT IGNORE INTO Manages (MatchID, ManagerName) VALUES (%s, %s)"
    cursor.executemany(sql, data)
    db_connection.commit()
    print("Manages table data insertion complete. {} rows processed.".format(len(data)))

def extract_data_from_csv(csv_file_path):
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        team_data = []
        player_data = []
        manager_data = []
        referee_data = []
        event_data = []
        football_match_data = []
        plays_data = []
        manages_data = []
        for row in csv_reader:
            # Extracting team data
            team_data.append(row['home_team'])
            team_data.append(row['away_team'])
            
            # Extracting player data
            player_data.append((row['home_captain'], True))
            player_data.append((row['away_captain'], True))
            
            # Extracting manager data
            manager_data.append(row['home_manager'])
            manager_data.append(row['away_manager'])
            
            # Extracting referee data
            referee_data.append(row['Referee'])
            
            # Extracting event data
            event_data.append((row['EventID'], row['EventYear'], row['EventHost'], row['NoTeams'], row['Champion'], row['RunnerUp'], row['TopScorer'], row['EventAttendance'], row['EventAttendanceAvg'], row['NoMatches']))
            
            # Extracting football match data
            football_match_data.append((row['MatchID'], row['home_score'], row['away_score'], row['home_penalty'], row['away_penalty'], row['Attendance'], row['Venue'], row['Round'], row['MatchDate'], row['Notes'], row['MatchHost'], row['EventID'], row['Referee']))
            
            # Extracting plays data
            plays_data.append((row['MatchID'], row['home_team']))
            plays_data.append((row['MatchID'], row['away_team']))
            
            # Extracting manages data
            manages_data.append((row['MatchID'], row['home_manager']))
            manages_data.append((row['MatchID'], row['away_manager']))
        
    return team_data, player_data, manager_data, referee_data, event_data, football_match_data, plays_data, manages_data

def insert_data(cursor, db_connection):
    print("Starting data insertion process...")
    
    # File path to CSV file
    csv_file_path = './Program/bigDataCleaned1.csv'
    
    try:
        team_data, player_data, manager_data, referee_data, event_data, football_match_data, plays_data, manages_data = extract_data_from_csv(csv_file_path)
                
        # Insert data into tables
        insert_into_team(cursor, db_connection, team_data)
        insert_into_player(cursor, db_connection, player_data)
        insert_into_manager(cursor, db_connection, manager_data)
        insert_into_referee(cursor, db_connection, referee_data)
        insert_into_event(cursor, db_connection, event_data)
        insert_into_football_match(cursor, db_connection, football_match_data)
        insert_into_plays(cursor, db_connection, plays_data)
        insert_into_manages(cursor, db_connection, manages_data)
        
        print("Data insertion complete.")
    except Exception as e:
        print("An error occurred during the data insertion process.")
        print("Error: {}".format(str(e)))

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
   