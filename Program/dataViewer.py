"""
Author: Ryan Mackintosh
Student ID: 21171466
Title: dataViewer.py
Purpose: View contents of a csv file
Date: 7 November 2023

References:
- "FOP Sem2 2023 LectureSlides" for fundamental programming concepts and exception handling.
- "DS Sem2 2023 Lecture Slides" for database concepts and SQL usage.
- W3Schools Python MySQL Tutorial: https://www.w3schools.com/python/python_mysql_getstarted.asp for practical MySQL operations with Python.
- Additional online resources as necessary for intermediate and advanced code concepts.
"""

import pandas as pd
import os

# Reference: "FOP Sem2 2023 LectureSlides" (for file handling in Python)
# Reference: "DS Sem2 2023 Lecture Slides" (for data manipulation with pandas)
def view_csv_data(file_path):
    if not os.path.isfile(file_path):
        print("Error: File not found. Please make sure the file path is correct.")
        return

    try:
        # Read the CSV file
        # Reference: "DS Sem2 2023 Lecture Slides" (for reading and displaying data using pandas)
        df = pd.read_csv(file_path)
        
        # Display column headers
        # Reference: "DS Sem2 2023 Lecture Slides" (for understanding data structures and dataframe operations)
        print("\nColumn Headers:")
        print(df.columns.tolist())
        
        # Display first 3 rows of each column
        # Reference: "DS Sem2 2023 Lecture Slides" (for basic data viewing and slicing techniques)
        print("\nFirst 3 rows of each column:")
        print(df.head(3))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    # Reference: "FOP Sem2 2023 LectureSlides" (for control structures and user input in Python)
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
    # Reference: "FOP Sem2 2023 LectureSlides" (for Python script execution model)
    print("This script is not meant to be run directly.")
    print("Please run this script through the main menu.")
