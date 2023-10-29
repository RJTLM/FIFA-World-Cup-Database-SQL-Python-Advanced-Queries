import pandas as pd # Ensure you have the pandas library installed. You can install it using pip: pip install pandas

def split_columns(input_file, output_file, columns_to_split):
    # Read the CSV file
    df = pd.read_csv(input_file)
    # Reference: pandas.read_csv documentation
    # https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
    
    # Print the column names to verify they are being read correctly
    print("Original columns:", df.columns.tolist())
    
    for column, delimiter in columns_to_split.items():
        # Check if column is in the dataframe
        if column not in df.columns:
            print(f"Error: '{column}' column not found in the input file")
            continue
        
        # Split the column into a new dataframe
        split_data = df[column].str.split(delimiter, expand=True)
        
        # Get the number of parts (columns after split)
        num_parts = split_data.shape[1]
        
        # Ask user for new column names
        new_column_names = []
        for i in range(num_parts):
            new_column_name = input(f"Enter the name for part {i+1} of the '{column}' column after splitting: ")
            new_column_names.append(new_column_name)
        
        # Rename the new columns
        split_data.columns = new_column_names
        
        # Concatenate the new columns to the original dataframe
        df = pd.concat([df, split_data], axis=1)
        
        # Drop the original column
        df = df.drop(columns=[column])
    
    # Write the updated dataframe to a new CSV file
    df.to_csv(output_file, index=False)
    print("Updated columns:", df.columns.tolist())
    print("Data successfully saved to", output_file)
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding data manipulation and pandas library in Python)

def main():
    # Get user inputs
    input_file = input("Enter the name of the CSV file: ")
    output_file = input("Enter the name of the output CSV file: ")
    
    columns_to_split = {}
    while True:
        column = input("Enter the name of the column to split (or 'done' to finish): ")
        if column.lower() == 'done':
            break
        delimiter = input(f"Enter the delimiter for splitting the '{column}' column: ")
        columns_to_split[column] = delimiter
    
    # Run the function
    split_columns(input_file, output_file, columns_to_split)
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding functions and user interactions in Python)

if __name__ == "__main__":
    main()
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding the main function and script execution in Python)
