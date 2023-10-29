import pandas as pd
import os

def view_csv_data(file_path):
    if not os.path.isfile(file_path):
        print("Error: File not found. Please make sure the file path is correct.")
        return

    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Display column headers
        print("\nColumn Headers:")
        print(df.columns.tolist())
        
        # Display first 3 rows of each column
        print("\nFirst 3 rows of each column:")
        print(df.head(3))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    while True:
        print("\nCSV File Viewer")
        print("1: View CSV File")
        print("0: Return to Main Menu")
        choice = input().strip()
        
        if choice == "1":
            file_path = input("Enter the path to the CSV file: ").strip()
            view_csv_data(file_path)
        elif choice == "0":
            print()
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
