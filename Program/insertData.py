import csv

def insert_into_country(cursor, db_connection, data):
    if not data:
        print("No data to insert into Country table.")
        return
    
    print("Inserting data into Country table...")
    sql = "INSERT IGNORE INTO Country (CountryName) VALUES (%s)"
    cursor.executemany(sql, [(country,) for country in set(data)])  # Using set to remove duplicates
    db_connection.commit()
    print("Country table data insertion complete. {} rows processed.".format(len(set(data))))

def insert_into_coach(cursor, db_connection, data):
    if not data:
        print("No data to insert into Coach table.")
        return
    
    # Remove duplicates and filter out empty strings
    unique_coach_names = set(filter(None, data))
    
    print("Inserting data into Coach table...")
    sql = "INSERT IGNORE INTO Coach (CoachName) VALUES (%s)"
    cursor.executemany(sql, [(coach_name,) for coach_name in unique_coach_names])
    db_connection.commit()
    print("Coach table data insertion complete. {} rows processed.".format(len(unique_coach_names)))

def insert_into_team(cursor, db_connection, data):
    if not data:
        print("No data to insert into Team table.")
        return
    
    # Remove duplicates
    unique_team_names = set(data)
    
    print("Inserting data into Team table...")
    sql = "INSERT IGNORE INTO Team (TeamName) VALUES (%s)"
    cursor.executemany(sql, [(team_name,) for team_name in unique_team_names])
    db_connection.commit()
    print("Team table data insertion complete. {} rows processed.".format(len(unique_team_names)))

# Add similar functions for other tables

def insert_data(cursor, db_connection):
    print("Starting data insertion process...")
    
    # File path to your CSV file
    csv_file_path = './Program/bigDataCleaned.csv'
    
    try:
        # Read data from CSV file and insert into tables
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            country_data = []
            coach_data = []
            team_data = []
            # Add similar lists for other tables

            for row in csv_reader:
                # Collect data for Country table
                country_data.append(row['EventHost'])
                                
                # Collect data for Coach table
                coach_data.append(row['home_manager'])
                coach_data.append(row['away_manager'])

                # Collect data for Team table
                team_data.append(row['home_team'])
                team_data.append(row['away_team'])


                # Collect similar data here for other tables
                # ...

            # Insert data into tables
            insert_into_country(cursor, db_connection, country_data)
            insert_into_coach(cursor, db_connection, coach_data)
            insert_into_team(cursor, db_connection, team_data)

            # Add similar calls for other tables

            print("Data insertion complete. {} rows processed.".format(len(country_data)))
    except Exception as e:
        print("An error occurred during the data insertion process.")
        print("Error: {}".format(str(e)))
