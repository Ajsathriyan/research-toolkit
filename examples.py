# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 21:36:47 2026

@author: AJITH
"""

# -*- coding: utf-8 -*-
"""
examples.py

Example usage of Research Toolkit.

Author: AJITH
"""

import pandas as pd

from modules import *

# ==========================================================
# Load Data
# ==========================================================

df = pd.read_excel("sample_data.xlsx")

# ==========================================================
# Descriptive Statistics
# ==========================================================

stats = descriptive_statistics(df)
print(stats)

export_dataframe(stats, "Descriptive_Statistics.xlsx")

# ==========================================================
# Paired t-test
# ==========================================================

result = paired_t_test(df, "Plan_A", "Plan_B")
print_test_result(result)

# ==========================================================
# Wilcoxon Test
# ==========================================================

result = wilcoxon_test(df, "Plan_A", "Plan_B")
print_test_result(result)

# ==========================================================
# Independent Test (Auto)
# ==========================================================

result = auto_independent_test(df, "Group1", "Group2")
print_test_result(result)

# ==========================================================
# Correlation (Auto)
# ==========================================================

result = auto_correlation(df, "MCSv", "GI")
print_test_result(result)

# ==========================================================
# Linear Regression
# ==========================================================

result = linear_regression(df, "MCSv", "GI")

print("\nLinear Regression")
print(result)

# ==========================================================
# Graphs
# ==========================================================

histogram(df, "MCSv")

box_plot(df, "GI")

scatter_plot(df, "MCSv", "GI")

regression_plot(df, "MCSv", "GI")

qq_plot(df, "MCSv")

bland_altman_plot(df, "Plan_A", "Plan_B")