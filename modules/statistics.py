# -*- coding: utf-8 -*-
"""
Created on Mon Jul 6 00:02:05 2026

@author: AJITH
"""

import pandas as pd
from modules.validation import (
    validate_column_exists,
    validate_numeric,
    validate_minimum_samples,
    validate_no_zero_variance,
)

from scipy.stats import (
    shapiro,
    ttest_rel,
    ttest_ind,
    wilcoxon,
    mannwhitneyu,
    pearsonr,
    spearmanr,
    linregress,
)

from modules.constants import IGNORE_COLUMNS


def descriptive_statistics(df):
    """
    Generate descriptive statistics for all numeric columns.
    """

    results = []

    # Select only numeric columns
    numeric_df = df.select_dtypes(include="number")

    numeric_df = numeric_df.drop(
        columns=[col for col in IGNORE_COLUMNS if col in numeric_df.columns],
        errors="ignore"
)

    # Calculate statistics
    for column in numeric_df.columns:

        data = numeric_df[column].dropna()

        mean = data.mean()
        sd = data.std()
        median = data.median()
        minimum = data.min()
        maximum = data.max()

        try:
            _, p = shapiro(data)
        except Exception:
            p = None

        results.append({
            "Variable": column,
            "Mean": round(mean, 3),
            "SD": round(sd, 3),
            "Median": round(median, 3),
            "Minimum": round(minimum, 3),
            "Maximum": round(maximum, 3),
            "Shapiro_p": round(p, 4) if p is not None else None
        })

    return pd.DataFrame(results)


def paired_t_test(df, column1, column2):
    """
    Perform a paired t-test.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    paired = df[[column1, column2]].dropna()

    data1 = paired[column1]
    data2 = paired[column2]

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)

    statistic, p = ttest_rel(data1, data2)

    return {
        "Test": "Paired t-test",
        "Variable 1": column1,
        "Variable 2": column2,
        "Test Statistic": round(float(statistic), 4),
        "p value": round(float(p), 4)
    }


def wilcoxon_test(df, column1, column2):
    """
    Perform Wilcoxon signed-rank test.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data  = df[[column1, column2]].dropna()

    data1 = data[column1]
    data2 = data[column2]

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)

    statistic, p = wilcoxon(data1, data2)

    return {
    "Test": "Wilcoxon Signed-Rank Test",
    "Variable 1": column1,
    "Variable 2": column2,
    "Test Statistic": round(float(statistic), 4),
    "p value": round(float(p), 4)
}


def independent_t_test(df, column1, column2):
    """
    Perform an independent t-test.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data1 = df[column1].dropna()
    data2 = df[column2].dropna()

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)


    statistic, p = ttest_ind(data1, data2, equal_var=False)

    return {
        "Test": "Independent t-test",
        "Variable 1": column1,
        "Variable 2": column2,
        "Test Statistic": round(float(statistic), 4),
        "p value": round(float(p), 4)
    }


def mann_whitney_test(df, column1, column2):
    """
    Perform Mann–Whitney U test.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data  = df[[column1, column2]].dropna()

    data1 = data[column1]
    data2 = data[column2]

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)


    statistic, p = mannwhitneyu(data1, data2, alternative="two-sided")

    return {
        "Test": "Mann-Whitney U Test",
        "Variable 1": column1,
        "Variable 2": column2,
        "Test Statistic": round(float(statistic), 4),
        "p value": round(float(p), 4)
    }


def auto_independent_test(df, column1, column2):
    """
    Automatically choose between independent t-test
    and Mann–Whitney U test.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data1 = df[column1].dropna()
    data2 = df[column2].dropna()

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)

    _, p1 = shapiro(data1)
    _, p2 = shapiro(data2)

    print(f"\nShapiro-Wilk ({column1}) p = {p1:.4f}")
    print(f"Shapiro-Wilk ({column2}) p = {p2:.4f}")
    
    if p1 >= 0.05 and p2 >= 0.05:
        print("Both groups are normally distributed.")
        result = independent_t_test(df, column1, column2)
    else:
        print("At least one group is NOT normally distributed.")
        result = mann_whitney_test(df, column1, column2)

    result["Normality p (Group 1)"] = round(float(p1), 4)
    result["Normality p (Group 2)"] = round(float(p2), 4)

    return result


def pearson_correlation(df, column1, column2):
    """
    Perform Pearson correlation.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data = df[[column1, column2]].dropna()

    data1 = data[column1]
    data2 = data[column2]

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)

    r, p = pearsonr(data1, data2)

    return {
        "Test": "Pearson Correlation",
        "Variable 1": column1,
        "Variable 2": column2,
        "Correlation": round(float(r), 4),
        "p value": round(float(p), 4)
    }


def spearman_correlation(df, column1, column2):
    """
    Perform Spearman correlation.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data = df[[column1, column2]].dropna()

    data1 = data[column1]
    data2 = data[column2]

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)

    r, p = spearmanr(data1, data2)

    return {
        "Test": "Spearman Correlation",
        "Variable 1": column1,
        "Variable 2": column2,
        "Correlation": round(float(r), 4),
        "p value": round(float(p), 4)
    }

def auto_correlation(df, column1, column2):
    """
    Automatically choose between Pearson and Spearman correlation.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data = df[[column1, column2]].dropna()

    data1 = data[column1]
    data2 = data[column2]

    validate_minimum_samples(data1)
    validate_minimum_samples(data2)

    validate_no_zero_variance(data1)
    validate_no_zero_variance(data2)

    _, p1 = shapiro(data1)
    _, p2 = shapiro(data2)

    print(f"\nShapiro-Wilk ({column1}) p = {p1:.4f}")
    print(f"Shapiro-Wilk ({column2}) p = {p2:.4f}")

    if p1 >= 0.05 and p2 >= 0.05:
        print("Both variables are normally distributed.")
        result = pearson_correlation(df, column1, column2)
    else:
        print("At least one variable is NOT normally distributed.")
        result = spearman_correlation(df, column1, column2)

    result["Normality p (Variable 1)"] = round(float(p1), 4)
    result["Normality p (Variable 2)"] = round(float(p2), 4)

    return result

def linear_regression(df, x_column, y_column):
    """
    Perform simple linear regression.
    """

    validate_column_exists(df, x_column)
    validate_column_exists(df, y_column)

    validate_numeric(df, x_column)
    validate_numeric(df, y_column)

    data = df[[x_column, y_column]].dropna()

    x = data[x_column]
    y = data[y_column]

    validate_minimum_samples(x)
    validate_minimum_samples(y)

    validate_no_zero_variance(x)
    validate_no_zero_variance(y)

    result = linregress(x, y)

    return {
    "Test": "Linear Regression",
    "Independent Variable": x_column,
    "Dependent Variable": y_column,
    "Slope": round(float(result.slope), 4),
    "Intercept": round(float(result.intercept), 4),
    "R": round(float(result.rvalue), 4),
    "R²": round(float(result.rvalue ** 2), 4),
    "p value": round(float(result.pvalue), 4),
    "Standard Error": round(float(result.stderr), 4)
}