
# -*- coding: utf-8 -*-
"""
Statistics Package

Author: AJITH
"""

# Statistics
from .statistics import (
    descriptive_statistics,
    paired_t_test,
    wilcoxon_test,
    independent_t_test,
    mann_whitney_test,
    auto_independent_test,
    pearson_correlation,
    spearman_correlation,
    auto_correlation,
    linear_regression,
)

# Graphs
from .graphs import (
    histogram,
    box_plot,
    scatter_plot,
    regression_plot,
    qq_plot,
    bland_altman_plot,
)

# Reporting
from .reporting import (
    print_test_result,
)

# Export
from .export import (
    export_dataframe,
    export_csv,
    export_dictionary,
    export_multiple,
)

# Validation
from .validation import (
    validate_column_exists,
    validate_numeric,
    validate_minimum_samples,
    validate_no_zero_variance,
)

# Constants
from .constants import (
    IGNORE_COLUMNS,
)

from modules import *

stats = descriptive_statistics(df)

result = paired_t_test(df, "ASC_OFF", "ASC_HIGH")
print_test_result(result)

regression_plot(df, "MCSv", "GI")

export_dataframe(stats, "Descriptive.xlsx")