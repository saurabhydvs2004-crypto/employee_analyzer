import pandas as pd
from pathlib import Path


class EmployeeAnalyzer:
    """Handles loading, analyzing, filtering, and exporting employee data."""

    def __init__(self, filepath: str):
        self.filepath = Path(filepath)
        self.df = None

    def load_data(self) -> None:
        """Loads employee CSV dataset into a Pandas DataFrame."""
        if not self.filepath.exists():
            raise FileNotFoundError(f"Source file not found at: {self.filepath}")
        
        self.df = pd.read_csv(self.filepath)
        # Standardize column headers
        self.df.columns = [col.strip().lower().replace(" ", "_") for col in self.df.columns]
        print(f"[+] Successfully loaded {len(self.df)} records from {self.filepath.name}")

    def calculate_metrics(self) -> dict:
        """Calculates average salary and department employee counts."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        avg_salary = self.df["salary"].mean()
        dept_counts = self.df["department"].value_counts().to_dict()

        return {
            "average_salary": round(avg_salary, 2),
            "department_counts": dept_counts
        }

    def filter_by_salary(self, threshold: float) -> pd.DataFrame:
        """Filters records where salary exceeds the specified threshold."""
        if self.df is None:
            raise ValueError("Data not loaded. Call load_data() first.")

        filtered_df = self.df[self.df["salary"] > threshold]
        return filtered_df

    def export_results(self, output_path: str, threshold: float) -> None:
        """Filters data and exports the filtered records to a new CSV file."""
        filtered_df = self.filter_by_salary(threshold)
        filtered_df.to_csv(output_path, index=False)
        print(f"[+] Exported {len(filtered_df)} filtered rows to: {output_path}")


def main():
    # 1. Setup sample data (if employee_data.csv does not already exist)
    sample_csv = "employee_data.csv"
    if not Path(sample_csv).exists():
        sample_data = {
            "name": ["Aarav", "Neha", "Rohan", "Pooja", "Vikram", "Sneha"],
            "department": ["IT", "HR", "IT", "Finance", "Finance", "HR"],
            "salary": [85000, 52000, 92000, 68000, 110000, 48000]
        }
        pd.DataFrame(sample_data).to_csv(sample_csv, index=False)
        print(f"[i] Generated mock dataset: {sample_csv}")

    # 2. Instantiate and run pipeline
    analyzer = EmployeeAnalyzer(filepath=sample_csv)
    analyzer.load_data()

    # 3. Calculate and display metrics
    metrics = analyzer.calculate_metrics()
    print("\n--- Summary Metrics ---")
    print(f"Average Salary: ${metrics['average_salary']}")
    print("Department Counts:")
    for dept, count in metrics["department_counts"].items():
        print(f"  * {dept}: {count}")

    # 4. Filter and export
    salary_cutoff = 60000.0
    output_csv = "high_earning_employees.csv"
    analyzer.export_results(output_path=output_csv, threshold=salary_cutoff)


if __name__ == "__main__":
    main()