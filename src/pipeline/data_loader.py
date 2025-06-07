import pandas as pd
import os

def load_data(path: str, target_column: str = "Default"):
    """
    Loads the dataset from the given path and separates features and target.

    Args:
        path (str): Relative or absolute path to the CSV file.
        target_column (str): Name of the target column. Defaults to "Default".

    Returns:
        X (pd.DataFrame): Feature matrix.
        y (pd.Series): Target variable.
    """
    # Resolve absolute file path
    abs_path = os.path.abspath(path)

    # Check if file exists
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"❌ File not found: {abs_path}")

    print(f"📂 Reading dataset from: {abs_path}")

    # Load CSV
    data = pd.read_csv(abs_path)

    # Check if file is empty
    if data.empty:
        raise ValueError("❌ Loaded dataset is empty. Please check the file contents.")

    # Drop identifier column if it exists
    if "LoanID" in data.columns:
        data.drop(columns=["LoanID"], inplace=True)

    # Check if target column exists
    if target_column not in data.columns:
        raise ValueError(f"❌ Target column '{target_column}' not found in dataset.")

    # Separate features and target
    X = data.drop(columns=[target_column])
    y = data[target_column]

    return X, y
