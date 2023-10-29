import pandas as pd

def split_officials_column(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Split the 'Officials' column into four new columns
    df[['Referee1', 'Referee2', 'Referee3', 'Referee4']] = df['Officials'].str.split(' \* ', expand=True)
    
    # Move the 'Referee' column to column "E"
    referee_col = df.pop('Referee')
    df.insert(4, 'Referee', referee_col)
    
    # Save the updated DataFrame to a new CSV file
    df.to_csv(output_file, index=False)
    print(f"Updated CSV file saved to {output_file}")

if __name__ == "__main__":
    input_file = 'Officials.csv'
    output_file = 'UpdatedOfficials.csv'
    split_officials_column(input_file, output_file)
