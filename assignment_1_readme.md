# ETL Pipeline for User Interaction Data

## Overview
This project ingests, cleans, transforms, and loads user interaction data from a CSV file into a SQL database for analysis.

## Steps
1. **Data Ingestion**: Read the CSV file into a DataFrame.
2. **Data Cleaning**: Handle missing values and ensure correct data types.
3. **Data Transformation**: Add a column for interaction counts.
4. **Data Loading**: Save the cleaned and transformed data into a SQLite database.

## How to Run
1. Setup virtual environment and Install dependencies:
    ```bash
    python3 -m venv venv
    pip install -r requirements.txt
    ```
   

2. Optional: To generate a test data run below script:
   ```
   python3 dags/generate_test_data.py
   ```

3. Execute the pipeline script:
    ```bash
    python3 assignment_1.py
    ```
   
4. Verify the database named ```datawarehouse-1.db``` using SQLite tools.
