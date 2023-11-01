# menu.py
import time  # Importing the time module for creating delays in output

def show_menu(first_time):
    if first_time:
        print("\nWelcome to the FIFA WWC Data Processing Program!")
    else:
        print("\nWelcome Back to the Main Menu!")
    print("What would you like to do?")
    print("1: View a CSV File")
    print("2: Clean Non-ASCII Characters from a CSV File")
    print("3: Extract or Update Columns in a CSV File")
    print("4: Split Columns in a CSV File")
    print("5: Insert Data into MySQL Database")
    print("0: Exit Program")
    choice = input().strip()  # Using strip to remove any leading or trailing whitespaces
    return choice
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding functions and user interactions in Python)
    # Reference: https://docs.python.org/3/library/stdtypes.html#str.strip (for understanding the strip function)

def main():
    first_time = True
    while True:
        choice = show_menu(first_time)
        if first_time:
            first_time = False
        if choice == "1":
            from dataViewer import main as view_csv
            view_csv()
        elif choice == "2":
            from asciiConversion import main as clean_ascii
            clean_ascii()
        elif choice == "3":
            from extractData import main as extract_data
            extract_data()
        elif choice == "4":
            from splitColumn import main as split_columns
            split_columns()
        elif choice == "5":
            from mySQLConnector import main as insert_data
            insert_data()
        elif choice == "0":
            print("Why do programmers like dark mode?")
            time.sleep(1.5)  # Wait for 1.5 seconds
            print("\nBecause light attracts bugs", end="", flush=True)
            time.sleep(3)  # Wait for 3 seconds
            print(".", end="", flush=True)
            time.sleep(0.75)  # Wait for 0.75 seconds
            print(".", end="", flush=True)
            time.sleep(0.75)  # Wait for 0.75 seconds
            print(".", end="", flush=True)
            time.sleep(0.75)  # Wait for 0.75 seconds
            print(" ", end="", flush=True)
            time.sleep(2)  # Wait for 2 seconds
            print("\n\nAnyway")
            time.sleep(1)  # Wait for 1 second
            print("Goodbye :)")
            break
        else:
            print("Invalid option. Please choose a valid option.")
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding control flow and modular programming in Python)
    # Reference: https://docs.python.org/3/library/time.html#time.sleep (for understanding the time.sleep function)

if __name__ == "__main__":
    main()
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding the main function and script execution in Python)
