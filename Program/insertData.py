import csv

def insert_into_country(cursor, db_connection, data):
    print(f"Inserting {data} into Country table...")
    sql = "INSERT IGNORE INTO Country (CountryName) VALUES (%s)"
    cursor.execute(sql, (data,))
    db_connection.commit()
    print(f"{data} inserted successfully.")

def insert_data(cursor, db_connection):
    print("Starting data insertion process...")
    
    # File path to your CSV file
    csv_file_path = './Program/bigDataCleaned.csv'
    
    try:
        # Read data from CSV file and insert into tables
        with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.DictReader(csvfile)
            row_count = 0
            for row in csv_reader:
                # Insert data into Country table
                # Assuming 'EventHost' column in CSV corresponds to 'CountryName' in Country table
                insert_into_country(cursor, db_connection, row['EventHost'])
                row_count += 1
                # Add similar code here to insert data into other tables
                # ...
            print(f"Data insertion complete. {row_count} rows processed.")
    except Exception as e:
        print("An error occurred during the data insertion process.")
        print(f"Error: {str(e)}")
