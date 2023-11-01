import csv

def insert_into_country(cursor, db_connection, data):
    if not data:
        print("No data to insert into Country table.")
        return
    
    print("Inserting data into Country table...")
    sql = "INSERT IGNORE INTO Country (CountryName) VALUES (%s)"
    cursor.executemany(sql, [(country,) for country in data])
    db_connection.commit()
    print("Country table data insertion complete. {} rows processed.".format(len(data)))

def insert_data(cursor, db_connection):
    print("Starting data insertion process...")
    
    # File path to your CSV file
    csv_file_path = './Program/bigDataCleaned.csv'
    
    try:
        # Read data from CSV file and insert into tables
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            country_data = []
            row_count = 0
            for row in csv_reader:
                # Collect data for Country table
                # Assuming 'EventHost' column in CSV corresponds to 'CountryName' in Country table
                country_data.append(row['EventHost'])
                row_count += 1
                # Collect similar data here for other tables
                # ...

            # Insert data into Country table
            insert_into_country(cursor, db_connection, country_data)
            # Insert similar data here for other tables
            # ...

            print("Data insertion complete. {} rows processed.".format(row_count))
    except Exception as e:
        print("An error occurred during the data insertion process.")
        print("Error: {}".format(str(e)))
