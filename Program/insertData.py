import csv

def insert_into_country(cursor, db_connection, data):
    sql = "INSERT IGNORE INTO Country (CountryName) VALUES (%s)"
    cursor.execute(sql, (data,))
    db_connection.commit()

def insert_data(cursor, db_connection):
    # File path to your CSV file
    csv_file_path = './Program/bigDataCleaned.csv'

    # Read data from CSV file and insert into tables
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            # Insert data into Country table
            # Assuming 'EventHost' column in CSV corresponds to 'CountryName' in Country table
            insert_into_country(cursor, db_connection, row['EventHost'])
            # Add similar code here to insert data into other tables
            # ...

    print("Data insertion complete.")
