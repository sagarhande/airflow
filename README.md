# ETL Pipeline for User Interaction Data

## Overview
This project ingests, cleans, transforms, and loads user interaction data from a CSV file into a SQL database for analysis.

## Steps
1. **Data Ingestion**: Read the CSV file into a DataFrame.
2. **Data Cleaning**: Handle missing values and ensure correct data types.
3. **Data Transformation**: Add a column for interaction counts.
4. **Data Loading**: Save the cleaned and transformed data into a SQLite database.

## Files
- `data_ingestion.py`: Script for data ingestion.
- `data_cleaning.py`: Script for data cleaning.
- `data_transformation.py`: Script for data transformation.
- `data_loading.py`: Script for data loading.
- `interaction_data.csv`: Sample input data file.
- `datawarehouse.db`: SQLite database file.

## How to Run
1. Install dependencies:
    ```bash
    pip install pandas sqlite3
    ```
2. Execute the pipeline script:
    ```bash
    python main.py
    ```

3. Verify the database using SQLite tools.
