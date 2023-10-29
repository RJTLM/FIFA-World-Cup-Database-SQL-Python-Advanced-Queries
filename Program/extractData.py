import csv
import os

def clean_data(data):
    """Clean the data by removing leading and trailing whitespaces."""
    return [item.strip() for item in data]

def extract_columns(data, column_names):
    """Extract specific columns from the data."""
    header = data[0]
    column_indices = [header.index(name) if name in header else None for name in column_names]
    extracted_data = [column_names]
    for row in data[1:]:
        extracted_row = [row[index] if index is not None else '' for index in column_indices]
        extracted_data.append(extracted_row)
    return extracted_data

def update_csv_file(filename, new_data):
    """Update the CSV file with new data. Add new columns or update existing ones."""
    if not os.path.exists(filename):
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(new_data)
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        existing_data = [row for row in reader]
    
    existing_header = existing_data[0]
    new_header = new_data[0]
    
    # Mapping of column name to its index in existing data
    existing_columns = {name: index for index, name in enumerate(existing_header)}
    
    # Add new columns to existing data
    for column in new_header:
        if column not in existing_columns:
            existing_columns[column] = len(existing_header)
            existing_header.append(column)
            for row in existing_data[1:]:
                row.append('')
    
    # Update existing data with new data
    for i, new_row in enumerate(new_data[1:], start=1):
        if i < len(existing_data):
            for column, new_value in zip(new_header, new_row):
                existing_data[i][existing_columns[column]] = new_value
        else:
            # If new data has more rows than existing data, add new rows
            new_row_extended = [''] * len(existing_header)
            for column, new_value in zip(new_header, new_row):
                new_row_extended[existing_columns[column]] = new_value
            existing_data.append(new_row_extended)
    
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(existing_data)

if __name__ == "__main__":
    input_filename = input("Enter the name of the CSV file to process: ")

    # Load the data into memory
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            reader = csv.reader(infile)
            data = [clean_data(row) for row in reader]
    except FileNotFoundError:
        print(f"The file {input_filename} was not found.")
        exit()

    # List column headers
    headers = data[0]
    print("Column headers:")
    for header in headers:
        print(header)

    while True:
        # Give user the option to exit or extract data
        choice = input("Choose an option:\n1. Exit\n2. Extract Data to a New CSV File\n3. Update or Add Columns in an Existing CSV File\n")
        if choice == "1":
            break
        elif choice in ["2", "3"]:
            column_names = input("Enter the names of the columns you wish to extract (separated by commas): ").split(',')
            column_names = [name.strip() for name in column_names]
            cleaned_data = extract_columns(data, column_names)
            
            if cleaned_data is not None:
                if choice == "2":
                    output_filename = input("Enter the name for the new CSV file: ")
                    with open(output_filename, 'w', newline='', encoding='utf-8') as outfile:
                        writer = csv.writer(outfile)
                        writer.writerows(cleaned_data)
                    print(f"Data saved to {output_filename}")
                else:
                    output_filename = input("Enter the name of the existing CSV file to update or add columns: ")
                    update_csv_file(output_filename, cleaned_data)
                    print(f"Data updated in {output_filename}")
            else:
                print("Operation aborted.")
        else:
            print("Invalid option. Please choose a valid option.")
