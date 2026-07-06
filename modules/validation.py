
# -*- coding: utf-8 -*-
"""
Validation functions for AJ Research Toolkit
"""

import pandas as pd


def validate_column_exists(df, column):
    """Check if a column exists."""
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found.")


def validate_numeric(df, column):
    """Check if a column contains numeric data."""
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' is not numeric.")


def validate_minimum_samples(data, minimum=3):
    """Check minimum number of observations."""
    if len(data.dropna()) < minimum:
        raise ValueError(
            f"At least {minimum} observations are required."
        )


def validate_no_zero_variance(data):
    """Check if all values are identical."""
    if data.nunique() <= 1:
        raise ValueError(
            "All values are identical. Statistical test cannot be performed."
        )