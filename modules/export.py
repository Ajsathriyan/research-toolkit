
# -*- coding: utf-8 -*-
"""
export.py

Functions for exporting statistical results.

Author: AJITH
"""

import pandas as pd


def export_dataframe(df, filename, index=False):
    """
    Export a DataFrame to Excel.

    Parameters
    ----------
    df : pandas.DataFrame
    filename : str
        Output Excel file.
    index : bool
        Write row index.
    """

    df.to_excel(filename, index=index)

    print(f"Saved: {filename}")


def export_csv(df, filename, index=False):
    """
    Export a DataFrame to CSV.
    """

    df.to_csv(filename, index=index)

    print(f"Saved: {filename}")


def export_dictionary(result, filename):
    """
    Export a dictionary to Excel.

    Useful for:
        - t-test
        - Wilcoxon
        - Correlation
        - Regression
    """

    df = pd.DataFrame([result])

    df.to_excel(filename, index=False)

    print(f"Saved: {filename}")


def export_multiple(results, filename):
    """
    Export multiple result dictionaries.

    Parameters
    ----------
    results : list of dict
    filename : str
    """

    df = pd.DataFrame(results)

    df.to_excel(filename, index=False)

    print(f"Saved: {filename}")