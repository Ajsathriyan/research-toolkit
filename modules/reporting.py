# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 00:27:32 2026

@author: AJITH
"""

def print_test_result(result):

    print("=" * 50)
    print(result["Test"])
    print("=" * 50)

    if result["Test"] == "Linear Regression":

        print(f"Independent Variable : {result['Independent Variable']}")
        print(f"Dependent Variable   : {result['Dependent Variable']}")
        print(f"Slope               : {result['Slope']}")
        print(f"Intercept           : {result['Intercept']}")
        print(f"R                   : {result['R']}")
        print(f"R²                  : {result['R²']}")
        print(f"Standard Error      : {result['Standard Error']}")
        print(f"p value             : {result['p value']}")

    else:

        print(f"Variable 1 : {result['Variable 1']}")
        print(f"Variable 2 : {result['Variable 2']}")

        if "Test Statistic" in result:
            print(f"Test Statistic : {result['Test Statistic']}")

        if "Correlation" in result:
            print(f"Correlation    : {result['Correlation']}")

        print(f"p value        : {result['p value']}")

        if "Normality p (Group 1)" in result:
            print(f"Normality G1   : {result['Normality p (Group 1)']}")
            print(f"Normality G2   : {result['Normality p (Group 2)']}")

        if "Normality p (Variable 1)" in result:
            print(f"Normality V1   : {result['Normality p (Variable 1)']}")
            print(f"Normality V2   : {result['Normality p (Variable 2)']}")

        print()

        if result["p value"] < 0.05:
            print("Interpretation: Statistically Significant (p < 0.05)")
        else:
            print("Interpretation: Not Statistically Significant (p ≥ 0.05)")