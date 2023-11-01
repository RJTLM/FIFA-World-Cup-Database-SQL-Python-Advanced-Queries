import mysql.connector
import csv
import getpass

# Database configuration
db_config = {
    'host': 'your_host',
    'user': input("Enter your MySQL username: "),
    'password': getpass.getpass("Enter your MySQL password: "),
    'database': 'your_database_name'
}

# Establish a database connection
db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

# File path to your CSV file
csv_file_path = './Program/bigDataCleaned.csv'

# Function to insert data into Country table
def insert_into_country(data):
    sql = "INSERT INTO Country (CountryName) VALUES (%s)"
    cursor.execute(sql, (data,))
    db_connection.commit()

# Read data from CSV file and insert into tables
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        # Insert data into Country table
        # Assuming 'EventHost' column in CSV corresponds to 'CountryName' in Country table
        insert_into_country(row['EventHost'])

        # Add similar code here to insert data into other tables
        # ...

# Close the cursor and database connection
cursor.close()
db_connection.close()
