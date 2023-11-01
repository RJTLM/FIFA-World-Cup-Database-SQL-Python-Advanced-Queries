import csv
from mySQLConnector import connect_to_db

def insert_into_country(cursor, db_connection, data):
    sql = "INSERT IGNORE INTO Country (CountryName) VALUES (%s)"
    cursor.execute(sql, (data,))
    db_connection.commit()

def main():
    cursor, db_connection = connect_to_db()

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

    # Close the cursor and database connection
    cursor.close()
    db_connection.close()
    print("Data insertion complete.")
