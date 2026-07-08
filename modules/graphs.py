# -*- coding: utf-8 -*-
"""
graphs.py

Statistical plotting functions.

Author: AJITH
"""

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import linregress, probplot

from modules.validation import (
    validate_column_exists,
    validate_numeric,
)

CURRENT_FIGURE = None
# ==========================================================
# Histogram
# ==========================================================

def histogram(df, column, bins=10):
    """
    Draw histogram.
    """

    validate_column_exists(df, column)
    validate_numeric(df, column)

    data = df[column].dropna()

    fig = plt.figure(figsize=(6,5), dpi=300)
    plt.hist(data, bins=bins)

    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.title(f"Histogram: {column}")

    plt.tight_layout()
    global CURRENT_FIGURE
    CURRENT_FIGURE = fig
    plt.show()


# ==========================================================
# Box Plot
# ==========================================================

def box_plot(df, column):
    """
    Draw box plot.
    """

    validate_column_exists(df, column)
    validate_numeric(df, column)

    data = df[column].dropna()

    fig = plt.figure(figsize=(6,5), dpi=300)
    plt.boxplot(data)

    plt.ylabel(column)
    plt.title(f"Box Plot: {column}")

    plt.tight_layout()
    global CURRENT_FIGURE
    CURRENT_FIGURE = fig
    plt.show()


# ==========================================================
# Scatter Plot
# ==========================================================

def scatter_plot(
    df,
    x_column,
    y_column,
    color="blue",
    marker="o",
    size=50
):
    """
    Draw scatter plot.
    """

    validate_column_exists(df, x_column)
    validate_column_exists(df, y_column)

    validate_numeric(df, x_column)
    validate_numeric(df, y_column)

    data = df[[x_column, y_column]].dropna()

    fig = plt.figure(figsize=(6,5), dpi=300)

    plt.scatter(
        data[x_column],
        data[y_column],
        color=color,
        marker=marker,
        s=size
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title("Scatter Plot")

    plt.tight_layout()
    global CURRENT_FIGURE
    CURRENT_FIGURE = fig
    plt.show()
# ==========================================================
# Regression Plot
# ==========================================================

def regression_plot(df, x_column, y_column):
    """
    Scatter plot with regression line.
    """

    validate_column_exists(df, x_column)
    validate_column_exists(df, y_column)

    validate_numeric(df, x_column)
    validate_numeric(df, y_column)

    data = df[[x_column, y_column]].dropna()

    x = data[x_column]
    y = data[y_column]

    result = linregress(x, y)

    fig = plt.figure(figsize=(6,5), dpi=300)

    plt.scatter(x, y)

    plt.plot(
        x,
        result.intercept + result.slope*x,
        linewidth=2
    )

    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title("Linear Regression")

    plt.tight_layout()
    global CURRENT_FIGURE
    CURRENT_FIGURE = fig
    plt.show()


# ==========================================================
# Q-Q Plot
# ==========================================================

def qq_plot(df, column):
    """
    Q-Q plot for normality.
    """

    validate_column_exists(df, column)
    validate_numeric(df, column)

    data = df[column].dropna()

    fig = plt.figure(figsize=(6,5), dpi=300)

    probplot(data, dist="norm", plot=plt)

    plt.title(f"Q-Q Plot: {column}")

    plt.tight_layout()
    global CURRENT_FIGURE
    CURRENT_FIGURE = fig
    plt.show()


# ==========================================================
# Bland-Altman Plot
# ==========================================================

def bland_altman_plot(df, column1, column2):
    """
    Bland-Altman plot.
    """

    validate_column_exists(df, column1)
    validate_column_exists(df, column2)

    validate_numeric(df, column1)
    validate_numeric(df, column2)

    data = df[[column1, column2]].dropna()

    x = data[column1]
    y = data[column2]

    mean = (x + y) / 2
    diff = x - y

    md = np.mean(diff)
    sd = np.std(diff, ddof=1)

    upper = md + 1.96 * sd
    lower = md - 1.96 * sd

    fig = plt.figure(figsize=(6,5), dpi=300)

    plt.scatter(mean, diff)

    plt.axhline(md, linestyle='-')
    plt.axhline(upper, linestyle='--')
    plt.axhline(lower, linestyle='--')

    plt.xlabel("Mean")
    plt.ylabel("Difference")
    plt.title("Bland-Altman Plot")

    plt.tight_layout()
    global CURRENT_FIGURE
    CURRENT_FIGURE = fig
    plt.show()