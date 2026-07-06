# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:16:18 2026

@author: AJITH
"""

# -*- coding: utf-8 -*-
"""
Menu module
"""

def main_menu():

    print("\n" + "=" * 50)
    print("AJ Research Toolkit")
    print("=" * 50)

    print("1. Descriptive Statistics")
    print("2. Paired Analysis")
    print("3. Independent Analysis")
    print("4. Correlation")
    print("5. Regression")
    print("6. Graphs")
    print("0. Exit")

    while True:

        try:
            choice = int(input("\nEnter your choice: "))

            if 0 <= choice <= 6:
                return choice

            print("Invalid choice.")

        except ValueError:
            print("Please enter a number.")