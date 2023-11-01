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

def insert_into_team(cursor, db_connection, data):
    if not data:
        print("No data to insert into Team table.")
        return
    
    print("Inserting data into Team table...")
    # Add your SQL insertion code here
    # ...

def insert_into_player(cursor, db_connection, data):
    if not data:
        print("No data to insert into Player table.")
        return
    
    print("Inserting data into Player table...")
    # Add your SQL insertion code here
    # ...

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
            team_data = []
            player_data = []
            # Add similar lists for other tables

            for row in csv_reader:
                # Collect data for Country table
                country_data.append(row['EventHost'])  # Assuming 'EventHost' column corresponds to 'CountryName'
                
                # Collect data for Team table
                # team_data.append(row['YourTeamColumn'])
                
                # Collect data for Player table
                # player_data.append(row['YourPlayerColumn'])
                
                # Collect similar data here for other tables
                # ...

            # Insert data into tables
            insert_into_country(cursor, db_connection, country_data)
            insert_into_team(cursor, db_connection, team_data)
            insert_into_player(cursor, db_connection, player_data)
            # Add similar calls for other tables

            print("Data insertion complete. {} rows processed.".format(len(country_data)))  # Update this line accordingly
    except Exception as e:
        print("An error occurred during the data insertion process.")
        print("Error: {}".format(str(e)))
