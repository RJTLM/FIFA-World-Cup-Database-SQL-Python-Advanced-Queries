import pandas as pd

def split_officials_column(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Print the column names to verify they are being read correctly
    print(df.columns)
    
    # Check if 'Officials' column is in the dataframe
    if 'Officials' not in df.columns:
        print("Error: 'Officials' column not found in the input file")
        return
    
    # Split the 'Officials' column into a new dataframe
    officials_split = df['Officials'].str.split(' \* ', expand=True)
    
    # Print the shape of officials_split to debug the issue
    print("Shape of officials_split:", officials_split.shape)
    
    # Get the number of referees (columns after split)
    num_referees = officials_split.shape[1]
    
    # Create dynamic column names based on the number of referees
    new_column_names = [f'Referee{i+1}' for i in range(num_referees)]
    
    # Rename the new columns
    officials_split.columns = new_column_names
    
    # Concatenate the new columns to the original dataframe
    df = pd.concat([df, officials_split], axis=1)
    
    # Drop the original 'Officials' column
    df = df.drop(columns=['Officials'])
    
    # Write the updated dataframe to a new CSV file
    df.to_csv(output_file, index=False)

# File paths
input_file = 'Officials.csv'
output_file = 'UpdatedOfficials.csv'

# Run the function
split_officials_column(input_file, output_file)
