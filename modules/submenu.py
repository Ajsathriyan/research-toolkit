# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 01:24:31 2026

@author: AJITH

"""
"""
Submenus
"""

def comparison_menu():

    print("\nCompare Two Groups")
    print("-" * 30)

    print("1. Paired Samples")
    print("2. Independent Samples")
    print("0. Back")

    while True:

        try:

            choice = int(input("\nEnter choice: "))

            if choice in [0,1,2]:
                return choice

            print("Invalid choice.")

        except ValueError:

            print("Please enter a number.")