import sys
import os

# Add 'src' to sys.path — now 'pipeline' becomes directly importable
sys.path.append(os.path.abspath('src'))

from pipeline.data_loader import load_data
from pipeline.preprocessor import get_preprocessor
from pipeline.transformer import transform_data

# Load data
X, y = load_data(r"C:\\Users\\bheem\\OneDrive\\Desktop\Data science Books\\cuap\second_sem\\ML\\Loan_default.csv")

# Build preprocessor
preprocessor = get_preprocessor(X)

# Transform data
X_processed = transform_data(preprocessor, X)

print(" Done. Transformed shape:", X_processed.shape)
