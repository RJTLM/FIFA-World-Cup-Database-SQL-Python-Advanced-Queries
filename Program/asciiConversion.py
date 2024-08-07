"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: asciiConversion.py
Purpose: Clean text in a csv file
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""
import csv
import unidecode  # Ensure you have the unidecode library installed. You can install it using pip: python3 -m pip install unidecode

# Reference: Unidecode on PyPI
# https://pypi.org/project/Unidecode/
# Description: This is the official Python Package Index (PyPI) page for the Unidecode library.

def clean_non_ascii(text):
    """Convert non-ASCII characters to their closest ASCII equivalents."""
    return unidecode.unidecode(text)
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding character encoding and string manipulation in Python)

def clean_csv(input_file, output_file):
    """Read a CSV file, clean non-ASCII characters, and write to a new file."""
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', newline='', encoding='utf-8') as outfile:
            reader = csv.reader(infile)
            writer = csv.writer(outfile)

            for row in reader:
                cleaned_row = [clean_non_ascii(cell) for cell in row]
                writer.writerow(cleaned_row)
        print(f"Cleaned CSV saved to {output_file}")
    except FileNotFoundError:
        print(f"The file {input_file} was not found. Please make sure the file exists and try again.")
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
        elif choice == "0":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid option. Please choose a valid option.")
    # Reference: "FOP Sem2 2023 Lecture Material" (for understanding the main function and script execution in Python)

if __name__ == "__main__":
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")

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
