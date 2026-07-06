from scipy.stats import shapiro
from modules.statistics import paired_t_test, wilcoxon_test
from modules.statistics import (
    independent_t_test,
    mann_whitney_test
)


def auto_independent_test(df, column1, column2):

    data1 = df[column1].dropna()
    data2 = df[column2].dropna()

    if len(data1) < 3 or len(data2) < 3:
        raise ValueError("Each group must contain at least 3 observations.")

    _, p1 = shapiro(data1)
    _, p2 = shapiro(data2)

    print(f"\nNormality p ({column1}) = {p1:.4f}")
    print(f"Normality p ({column2}) = {p2:.4f}")

    if p1 >= 0.05 and p2 >= 0.05:
        print("Both groups are normally distributed.")
        result = independent_t_test(df, column1, column2)
    else:
        print("At least one group is not normally distributed.")
        result = mann_whitney_test(df, column1, column2)

    result["Normality p (Group 1)"] = round(float(p1), 4)
    result["Normality p (Group 2)"] = round(float(p2), 4)

    return result

def auto_paired_test(df, column1, column2):

    paired = df[[column1, column2]].dropna()

    differences = paired[column1] - paired[column2]

    if len(differences) < 3:
        raise ValueError("At least 3 paired observations are required.")

    _, p_normality = shapiro(differences)

    print(f"\nNormality test (Shapiro-Wilk) p = {p_normality:.4f}")

    if p_normality >= 0.05:
        print("Data are normally distributed.")
        result = paired_t_test(df, column1, column2)
    else:
        print("Data are NOT normally distributed.")
        result = wilcoxon_test(df, column1, column2)

    result["Normality p"] = round(float(p_normality), 4)

    return result