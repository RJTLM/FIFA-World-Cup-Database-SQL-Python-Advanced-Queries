# menu.py
import time

def show_menu():
    print("\nWelcome to the Data Processing Menu!")
    print("What would you like to do?")
    print("1: View a CSV File")
    print("2: Clean Non-ASCII Characters from a CSV File")
    print("3: Extract or Update Columns in a CSV File")
    print("4: Split Columns in a CSV File")
    print("0: Exit Program")
    choice = input().strip()
    return choice
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding functions and user interactions in Python)

def main():
    while True:
        choice = show_menu()
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
        elif choice == "0":
            print("Why do programmers like dark mode?")
            time.sleep(1.5)  # Wait for 1.5 seconds
            print("\nBecause light attracts bugs", end="", flush=True)
            time.sleep(3)  # Wait for 1 second
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

if __name__ == "__main__":
    main()
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding the main function and script execution in Python)
