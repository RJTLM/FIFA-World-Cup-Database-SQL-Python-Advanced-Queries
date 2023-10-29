import csv
import unidecode # Ensure you have the unidecode library installed. You can install it using pip: pip install unidecode

# Reference: Unidecode on PyPI
# https://pypi.org/project/Unidecode/
# Description: This is the official Python Package Index (PyPI) page for the Unidecode library.
def clean_non_ascii(text):
    """Convert non-ASCII characters to their closest ASCII equivalents."""
    return unidecode.unidecode(text)
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding character encoding and string manipulation in Python)

def clean_csv(input_file, output_file):
    """Read a CSV file, clean non-ASCII characters, and write to a new file."""
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            cleaned_row = [clean_non_ascii(cell) for cell in row]
            writer.writerow(cleaned_row)
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding file I/O and CSV file manipulation in Python)

def main():
    while True:
        print("\nCSV File Cleaner")
        print("1: Clean a CSV File")
        print("0: Return to Main Menu")
        choice = input().strip()
        
        if choice == "1":
            input_filename = input("Enter the name of the CSV file to clean: ")
            output_filename = input("Enter the name for the cleaned CSV file: ")
            
            clean_csv(input_filename, output_filename)
            print(f"Cleaned CSV saved to {output_filename}")
        elif choice == "0":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option. Please choose a valid option.")
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding the main function and script execution in Python)

# Reference: How to use unidecode in python (3.3) - Stack Overflow
# https://stackoverflow.com/questions/19771751/how-to-use-unidecode-in-python-3-3
# Description: This Stack Overflow post discusses how to use the unidecode module in Python 3.

# Reference: Unicode HOWTO — Python 3.12.0 documentation
# https://docs.python.org/3/howto/unicode.html
# Description: This is the official Python documentation on Unicode. It provides a comprehensive overview of Unicode in Python.

# Reference: unicodedata — Unicode Database — Python 3.12.0 documentation
# https://docs.python.org/3/library/unicodedata.html
# Description: This module provides access to the Unicode Character Database (UCD) in Python.
