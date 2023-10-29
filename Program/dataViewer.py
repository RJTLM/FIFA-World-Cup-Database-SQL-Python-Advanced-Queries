import pandas as pd

def view_csv_data(file_path):
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
        print("0: Exit Program")
        choice = input("Please choose an option: ")
        
        if choice == "1":
            file_path = input("Enter the path to the CSV file: ")
            view_csv_data(file_path)
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
