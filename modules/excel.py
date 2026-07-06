# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 23:46:03 2026

@author: AJITH
"""

import pandas as pd


def load_excel(file_path):
    """
    Load an Excel file and return a pandas DataFrame.
    """

    try:
        df = pd.read_excel(file_path)

        print("Excel file loaded successfully.")
        return df

    except FileNotFoundError:
        print("Error: File not found.")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None