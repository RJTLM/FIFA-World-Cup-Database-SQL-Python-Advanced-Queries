import csv
import os

def clean_data(data):
    """Clean the data by removing leading and trailing whitespaces."""
    return [item.strip() for item in data]

def extract_columns(data, column_names):
    """Extract specific columns from the data."""
    header = data[0]
    missing_columns = [name for name in column_names if name not in header]
    if missing_columns:
        print(f"Columns {', '.join(missing_columns)} not found in the data.")
        return None
    
    column_indices = [header.index(name) for name in column_names]
    extracted_data = [column_names]
    for row in data[1:]:
        extracted_data.append([row[index] for index in column_indices])
    
    return extracted_data

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
        choice = input("Choose an option:\n1. Exit\n2. Extract Data to a New CSV File\n3. Append Data to an Existing CSV File\n")
        if choice == "1":
            break
        elif choice in ["2", "3"]:
            column_names = input("Enter the names of the columns you wish to extract (separated by commas): ").split(',')
            column_names = [name.strip() for name in column_names]
            cleaned_data = extract_columns(data, column_names)
            
            if cleaned_data is not None:
                if choice == "2":
                    output_filename = input("Enter the name for the new CSV file: ")
                    mode = 'w'
                else:
                    output_filename = input("Enter the name of the existing CSV file to append to: ")
                    mode = 'a' if os.path.exists(output_filename) else 'w'
                
                with open(output_filename, mode, newline='', encoding='utf-8') as outfile:
                    writer = csv.writer(outfile)
                    if mode == 'w' or os.path.getsize(output_filename) == 0:
                        writer.writerow(cleaned_data[0])  # Write header if file is empty
                    writer.writerows(cleaned_data[1:])
                
                print(f"Data saved to {output_filename}")
            else:
                print("Operation aborted.")
        else:
            print("Invalid option. Please choose a valid option.")
