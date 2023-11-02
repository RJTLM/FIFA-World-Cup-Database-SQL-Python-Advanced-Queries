#insertData.py

def execute_sql_file(cursor, file_path):
    with open(file_path, 'r') as file:
        sql_script = file.read()
        commands = sql_script.split(';')
        for command in commands:
            if command.strip() != "":
                cursor.execute(command)

def populate_other_tables(cursor):
    # Populate Team table
    cursor.execute("INSERT IGNORE INTO Team (TeamName) SELECT DISTINCT home_team FROM BigData WHERE home_team IS NOT NULL")
    cursor.execute("INSERT IGNORE INTO Team (TeamName) SELECT DISTINCT away_team FROM BigData WHERE away_team IS NOT NULL")

    # Populate Player table
    cursor.execute("INSERT IGNORE INTO Player (PlayerName) SELECT DISTINCT home_captain FROM BigData WHERE home_captain IS NOT NULL")
    cursor.execute("INSERT IGNORE INTO Player (PlayerName) SELECT DISTINCT away_captain FROM BigData WHERE away_captain IS NOT NULL")

    # Populate Manager table
    cursor.execute("INSERT IGNORE INTO Manager (ManagerName) SELECT DISTINCT home_manager FROM BigData WHERE home_manager IS NOT NULL")
    cursor.execute("INSERT IGNORE INTO Manager (ManagerName) SELECT DISTINCT away_manager FROM BigData WHERE away_manager IS NOT NULL")

    # Populate Referee table
    cursor.execute("INSERT IGNORE INTO Referee (RefereeName) SELECT DISTINCT Referee FROM BigData WHERE Referee IS NOT NULL")

    # Populate Event table
    cursor.execute("INSERT IGNORE INTO Event SELECT * FROM LittleData")

    # Populate FootballMatch table
    cursor.execute("""
        INSERT IGNORE INTO FootballMatch (MatchID, home_score, away_score, home_penalty, away_penalty, MatchAttendance, Venue, Round, MatchDate, Notes, MatchHost, EventID, RefereeName)
        SELECT b.MatchID, b.home_score, b.away_score, b.home_penalty, b.away_penalty, b.MatchAttendance, b.Venue, b.Round, b.MatchDate, b.Notes, b.MatchHost, e.EventID, b.Referee
        FROM BigData b
        JOIN Event e ON b.MatchYear = e.EventYear AND b.MatchHost = e.EventHost
    """)

    # Populate Plays table
    cursor.execute("""
        INSERT IGNORE INTO Plays (MatchID, TeamName)
        SELECT MatchID, home_team FROM BigData WHERE home_team IS NOT NULL
    """)
    cursor.execute("""
        INSERT IGNORE INTO Plays (MatchID, TeamName)
        SELECT MatchID, away_team FROM BigData WHERE away_team IS NOT NULL
    """)

    # Populate Manages table
    cursor.execute("""
        INSERT IGNORE INTO Manages (MatchID, ManagerName)
        SELECT MatchID, home_manager FROM BigData WHERE home_manager IS NOT NULL
    """)
    cursor.execute("""
        INSERT IGNORE INTO Manages (MatchID, ManagerName)
        SELECT MatchID, away_manager FROM BigData WHERE away_manager IS NOT NULL
    """)

def insert_data(cursor, db_connection):
    # Paths to the SQL insert files
    little_data_path = './Program/Tables/InsertTables/insLittleData.sql'
    big_data_path = './Program/Tables/InsertTables/insBigData.sql'

    # Executing the SQL insert files
    execute_sql_file(cursor, little_data_path)
    execute_sql_file(cursor, big_data_path)

    # Populating other tables based on the data in LittleData and BigData
    populate_other_tables(cursor)

    # Committing the changes
    db_connection.commit()

    print("Data insertion and table population completed successfully.")