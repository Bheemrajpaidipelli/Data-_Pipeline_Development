# Problem Statement
 Created a pipeline for data preprocessing, transformation, and loading using tools like pandas and Scikit-learn.

 # Table of Contents
1) problem satement 
2) project Structure
3) Functionality
4) Notes
5)Author

# Project Structure
Pipeline_creation/

│

├── data/

│ └── Loan_default.csv # Raw dataset used for 

testing the pipeline

│
├── notebooks/

│ └── DATA PIPELINE DEVELOPMENT.ipynb

│

├── src/

│ └── pipeline/

│ ├── init.py

│ ├── data_loader.py # Loads and splits the data

│ ├── preprocessor.py # Constructs the 
preprocessing pipeline

│ └── transformer.py # Applies preprocessing transformations

│
├── main.py # Main script to run the data pipeline

└── README.md # Project documentation



 # Functionality
 The pipeline performs the following steps:

1. **Loads the dataset** (`data_loader.py`)
2. **Drops unused columns** (e.g., `LoanID`)
3. **Splits features and target** (`X`, `y`)
4. **Defines preprocessing logic** using Scikit-learn pipelines (`preprocessor.py`)
5. **Applies preprocessing to data** (`transformer.py`)
6. **Returns cleaned and transformed data**

-Final output is printed with the transformed dataset's shape.

# Notes
* The pipeline is designed for reusability and modularity.

* No model training or prediction is included in this project.

* Suitable for integrating into any ML pipeline after preprocessing.

* File path issues are handled to support both Windows and relative paths.

# Author
Bheemrajpaidipelli