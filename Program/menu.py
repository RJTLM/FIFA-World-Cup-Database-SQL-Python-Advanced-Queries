# menu.py

def show_menu():
    print("\nWelcome to the Data Processing Menu!")
    print("1: Clean Non-ASCII Characters from CSV")
    print("2: Extract or Update Columns in a CSV File")
    print("3: Split Columns in a CSV File")
    print("0: Exit Program")
    choice = input("Please choose an option: ")
    return choice
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding functions and user interactions in Python)

def main():
    while True:
        choice = show_menu()
        if choice == "1":
            from asciiConversion import main as clean_ascii
            clean_ascii()
        elif choice == "2":
            from extractData import main as extract_data
            extract_data()
        elif choice == "3":
            from splitColumn import main as split_columns
            split_columns()
        elif choice == "0":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding control flow and modular programming in Python)

if __name__ == "__main__":
    main()
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding the main function and script execution in Python)
