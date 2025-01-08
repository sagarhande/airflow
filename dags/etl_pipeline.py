from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import pandas as pd
import sqlite3
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(script_dir, "interaction_data.csv")

def ingest_data(csv_file):
    print(f"Ingesting data from {csv_file}")
    try:
        data = pd.read_csv(csv_file)
        print("Data ingestion successful!")
        return data
    except Exception as e:
        print(f"Error occurred while ingesting data: {e}")
        return pd.DataFrame()


def clean_data(data):
    try:
        print("Cleaning data...")
        print(data.head())
        data = data.dropna()  # Option: fillna(value) for default values

        # Ensure correct data types
        data['timestamp'] = pd.to_datetime(data['timestamp'], errors='coerce')

        # Remove rows with invalid timestamps
        data = data.dropna(subset=['timestamp'])

        print("Data cleaning complete!")
        return data
    except Exception as e:
        print(f"Error occurred while cleaning data: {e}")
        return pd.DataFrame()


def transform_data(data):
    try:
        print("Transforming data...")

        # Calculate interaction counts per user and product
        user_counts = data['user_id'].value_counts()
        product_counts = data['product_id'].value_counts()

        # Map counts to a new column
        data['interaction_count'] = data['user_id'].map(user_counts) + data['product_id'].map(product_counts)

        print("Data transformation complete!")
        return data
    except Exception as e:
        print(f"Error occurred while transforming data: {e}")
        return pd.DataFrame()



def load_data_to_sql(data, db_name='datawarehouse.db', table_name='interactions'):
    print(f"Loading data into {db_name}, table: {table_name}")

    try:
        # Establish a connection to SQLite database
        conn = sqlite3.connect(db_name)

        # Load the DataFrame into the database
        data.to_sql(table_name, conn, if_exists='replace', index=False)

        print(f"Data loaded successfully into {db_name}!")
        conn.close()
    except Exception as e:
        print(f"Error loading data: {e}")


# Default arguments
default_args = {
    'owner': 'Sagar',
    'depends_on_past': False,
    'email': ['alert@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# DAG definition
with DAG(
    'etl_pipeline',
    default_args=default_args,
    description='An ETL pipeline for user interaction data',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 1, 1),
    catchup=False,
) as dag:

    # Task 1: Ingest data
    ingest_task = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data,
        op_args=[CSV_FILE],
    )


    # Task 2: Clean data
    def clean_data_wrapper(**context):
        # Pull the output from the previous task
        ingested_data = context['ti'].xcom_pull(task_ids='ingest_data')
        print("Context: ", context)
        return clean_data(ingested_data)


    clean_task = PythonOperator(
        task_id='clean_data',
        python_callable=clean_data_wrapper,
        provide_context=True,
    )


    # Task 3: Transform data
    def transform_data_wrapper(**context):
        # Pull the cleaned data from XCom
        cleaned_data = context['ti'].xcom_pull(task_ids='clean_data')
        return transform_data(cleaned_data)


    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data_wrapper,
        provide_context=True,
    )


    # Task 4: Load data
    def load_data_wrapper(**context):
        # Pull the transformed data from XCom
        transformed_data = context['ti'].xcom_pull(task_ids='transform_data')
        load_data_to_sql(transformed_data, db_name='datawarehouse-2.db', table_name='interactions')


    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data_wrapper,
        provide_context=True,
    )

    # Define task dependencies
    ingest_task >> clean_task >> transform_task >> load_task