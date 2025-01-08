# Airflow ETL Automation

This project utilizes Apache Airflow to automate the ETL (Extract, Transform, Load) process defined in the first assignment for user interaction data. This README details how to set up the Airflow environment and run the DAG that automates the ETL tasks.

## Project Structure

- `dags/` - Contains the Airflow DAG file(s).
- `requirements.txt` - Necessary Python packages for running the ETL scripts and Airflow.

## Getting Started

### Prerequisites

- Python 3.9
- Apache Airflow

### Clone the repository

     git clone https://github.com/sagarhande/airflow.git
     cd airflow

### Installation

1. **Install Airflow**:
   Apache Airflow requires a backend database, the example below uses default sqllite3.

   - Create virtual env and Install requirements:
     ```
     python3 -m venv venv
     source venv/bin/activate
     pip3 install -r requirements.txt
     ```
     
   - Initialize the Airflow Database
     ```
     airflow db init
     ```
   - Create a admin user for Airflow:
     ```
     airflow users create \
     --username admin \
     --firstname Admin \
     --lastname User \
     --role Admin \
     --email admin@example.com
     ```
   - Start the Airflow Services (Web Server and Scheduler)
     ```
     airflow webserver --port 8080
     airflow scheduler
     ```

2. **Set Up Your Airflow Home Directory**

    Airflow uses a directory structure for configurations, DAGs, logs, etc. By default, this is ~/airflow. You can override it by setting the AIRFLOW_HOME environment variable:
     ```
     export AIRFLOW_HOME=~/airflow
     ```

3. **Verify Installation**: 

   * Check the Airflow UI (localhost:8080) to ensure your DAGs are listed.
   * Trigger a DAG to confirm proper execution.

4. **Run the dag**:
   * from UI run the dag named ```etl_pipeline```
   * Once successful,verify newly created database named ```datawarehouse-2.db``` using SQLite tools. 
