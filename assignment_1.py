
from dags.etl_pipeline import *


def run():
    # Ingest data
    df = ingest_data(CSV_FILE)
    print(df.head())
    print("---------------------------------------------------")

    # Transform data
    cleaned_df = clean_data(df)
    print(cleaned_df.head())
    print("---------------------------------------------------")

    # Transform data
    transformed_df = transform_data(cleaned_df)
    print(transformed_df.head())
    print("---------------------------------------------------")

    # Load data
    load_data_to_sql(data=transformed_df, db_name="datawarehouse-1.db")

if __name__=="__main__":
    run()