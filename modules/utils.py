# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 00:35:58 2026

@author: AJITH
"""

def list_columns(df):
    """
    Display all columns except identifier columns.
    """

    ignore = ["Patient", "Patient_ID", "ID", "Case", "Serial", "S.No"]

    columns = [col for col in df.columns if col not in ignore]

    print("\nAvailable Columns")
    print("-" * 30)

    for i, col in enumerate(columns, start=1):
        print(f"{i}. {col}")

    return columns


def choose_columns(columns):
    """
    Allow the user to choose two different columns by number.
    """

    while True:
        try:
            first = int(input("\nSelect first column number : "))
            second = int(input("Select second column number: "))

            if first < 1 or first > len(columns):
                print("❌ Invalid first column number.")
                continue

            if second < 1 or second > len(columns):
                print("❌ Invalid second column number.")
                continue

            if first == second:
                print("❌ Please select two different columns.")
                continue

            return columns[first - 1], columns[second - 1]

        except ValueError:
            print("❌ Please enter valid numbers.")