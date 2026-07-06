# -*- coding: utf-8 -*-
"""
Created on Sun Jul 5 23:41:26 2026

@author: AJITH
"""

from modules.menu import main_menu
from modules.excel import load_excel
from modules.analysis import auto_paired_test
from modules.statistics import descriptive_statistics
from modules.reporting import print_test_result
from modules.utils import list_columns, choose_columns


def main():

    print("=" * 50)
    print("AJ RESEARCH TOOLKIT")
    print("=" * 50)

    file_path = input("Enter Excel file path: ")

    df = load_excel(file_path)

    if df is None:
        return

    print("\nFirst Five Rows\n")
    print(df.head())

    choice = main_menu()

    if choice == 1:

        print("\nDescriptive Statistics\n")

        stats = descriptive_statistics(df)
        print(stats)

    elif choice == 2:

        columns = list_columns(df)

        col1, col2 = choose_columns(columns)

        print("\nRunning Analysis...\n")

        result = auto_paired_test(df, col1, col2)

        print_test_result(result)

    elif choice == 0:

        print("\nGoodbye!")


if __name__ == "__main__":
    main()