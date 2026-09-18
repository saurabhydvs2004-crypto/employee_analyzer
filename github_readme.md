# Employee Data Analysis Tool

A Python-based data processing and analysis tool built for the **Week 4 Capstone Project (Automation / Data Handling)**. This project demonstrates Object-Oriented Programming (OOP), file handling, and tabular data manipulation using `pandas`.

---

## Features

- **Object-Oriented Design**: Encapsulates data ingestion, transformation, and reporting within a reusable `EmployeeAnalyzer` class.
- **Automated Data Ingestion**: Reads CSV datasets and standardizes column headers for seamless downstream processing.
- **Statistical Summaries**:
  - Calculates company-wide average salary.
  - Aggregates headcount distribution across departments.
- **Dynamic Filtering**: Filters records based on configurable salary thresholds.
- **Data Export**: Exports cleaned and filtered subsets into standalone CSV files for downstream reporting.
- **Built-in Mock Generator**: Automatically provisions sample data if an external dataset is not immediately available.

---

## Project Structure

```text
├── employee_analyzer.py      # Core script containing the EmployeeAnalyzer class and entry point
├── employee_data.csv         # Source input data (mock or Kaggle dataset)
├── high_earning_employees.csv# Output file generated after filtering
├── requirements.txt          # Project dependencies
└── README.md                 # Project documentation
```

---

## Prerequisites

- **Python**: Version 3.8 or higher
- **Pandas**: Version 1.3.0 or higher

Install the required dependencies using pip:

```bash
pip install pandas
```

Or via `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Run with Default / Mock Data
Run the script directly. If `employee_data.csv` is not present in the root directory, the script will generate a sample dataset automatically:

```bash
python employee_analyzer.py
```

### 2. Run with a Custom Dataset
1. Place your Kaggle employee dataset CSV inside the repository root.
2. Ensure your CSV includes at least the following columns: `name`, `department`, and `salary`.
3. Update the source filename in `employee_analyzer.py`:
   ```python
   sample_csv = "your_dataset.csv"
   ```
4. Run the script:
   ```bash
   python employee_analyzer.py
   ```

---

## Code Overview

```python
from employee_analyzer import EmployeeAnalyzer

# Initialize analyzer with dataset path
analyzer = EmployeeAnalyzer(filepath="employee_data.csv")

# Ingest and clean headers
analyzer.load_data()

# Compute summary statistics
metrics = analyzer.calculate_metrics()
print(f"Average Salary: ${metrics['average_salary']}")
print(f"Department Breakdown: {metrics['department_counts']}")

# Filter and export high earners
analyzer.export_results(output_path="filtered_output.csv", threshold=60000.0)
```

---

## Example Output

### Terminal Summary:
```text
[+] Successfully loaded 6 records from employee_data.csv

--- Summary Metrics ---
Average Salary: $75833.33
Department Counts:
  * IT: 2
  * HR: 2
  * Finance: 2
[+] Exported 4 filtered rows to: high_earning_employees.csv
```

### Exported CSV Sample (`high_earning_employees.csv`):
| name | department | salary |
| :--- | :--- | :--- |
| Aarav | IT | 85000 |
| Rohan | IT | 92000 |
| Pooja | Finance | 68000 |
| Vikram | Finance | 110000 |

---

## License

Distributed under the MIT License. See `LICENSE` for more information.