# Research Toolkit

Research Toolkit is a lightweight Python package for statistical analysis, data visualization, regression, correlation analysis, and automated reporting. It is designed for researchers, medical physicists, clinicians, and students working with scientific data.

Developed by **AJITH**

---

## Features

- Descriptive Statistics
- Paired t-test
- Independent t-test
- Wilcoxon Signed-Rank Test
- Mann–Whitney U Test
- Pearson Correlation
- Spearman Correlation
- Automatic Test Selection
- Linear Regression
- Histogram
- Box Plot
- Scatter Plot
- Regression Plot
- Q-Q Plot
- Bland–Altman Plot
- Excel Export
- CSV Export

---

## Installation

Clone the repository

```bash
git clone https://github.com/ajsathriyan/research-toolkit.git
```

Move into the project

```bash
cd research-toolkit
```

Install

```bash
pip install .
```

Or install requirements

```bash
pip install -r requirements.txt
```

---

## Dependencies

- Python 3.9+
- NumPy
- Pandas
- SciPy
- Matplotlib
- OpenPyXL

---

## Example

```python
import pandas as pd

from modules import *

df = pd.read_excel("data.xlsx")

stats = descriptive_statistics(df)

print(stats)

result = paired_t_test(df, "Plan_A", "Plan_B")

print_test_result(result)

regression_plot(df, "MCSv", "GI")
```

---

## Project Structure

```
research-toolkit/
│
├── modules/
│   ├── __init__.py
│   ├── constants.py
│   ├── validation.py
│   ├── statistics.py
│   ├── reporting.py
│   ├── graphs.py
│   └── export.py
│
├── examples.py
├── requirements.txt
├── setup.py
├── LICENSE
└── README.md
```

---

## Author

**AJITH**

Email: makumar735@gmail.com

GitHub: https://github.com/ajsathriyan

---

## License

This project is licensed under the MIT License.
