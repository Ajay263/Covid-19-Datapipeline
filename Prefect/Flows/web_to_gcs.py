import os
import pandas as pd
import numpy as np
import time
import pyarrow as pa
from random import randint
from pathlib import Path
from prefect import flow, task
from prefect.tasks import task_input_hash
from datetime import timedelta, datetime
from prefect_gcp.cloud_storage import GcsBucket
from prefect_gcp import GcpCredentials
from kaggle.api.kaggle_api_extended import KaggleApi
import logging
from prefect.filesystems import GCS


@task(retries=3,log_prints=True, tags=["extract"], cache_key_fn=task_input_hash, cache_expiration=timedelta(days=1))
def extract_data() -> pd.DataFrame:
    """
    Reads COVID-19 data from the local into a pandas DataFrame.

    Returns:
        pd.DataFrame: The DataFrame containing the COVID-19 data.

    Raises:
        Exception: If the data cannot be read into a DataFrame.
    """
    dataset_url = 'data/owid-covid-data.csv'
    try:      
        # Read the COVID-19 data from the local 
        df = pd.read_csv(dataset_url)

        # Return the DataFrame
        return df

    except Exception as e:
        # Log the error message and raise the exception
        logging.error(f"Failed to read data into Pandas DataFrame: {str(e)}")
        raise
    

@task(log_prints=True)
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans the input DataFrame by converting the 'date' column to datetime format.

    Args:
        df (pd.DataFrame): The input DataFrame to be cleaned.

    Returns:
        pd.DataFrame: The cleaned DataFrame.

    Raises:
        ValueError: If the input DataFrame is None or does not contain the 'date' column or has null values in the 'date' column.
    """
    try:
        # Check that the input DataFrame is not None and contains the 'date' column
        if df is None:
            raise ValueError("Input DataFrame is None")
        if 'date' not in df.columns:
            raise ValueError("Input DataFrame does not contain 'date' column")

        # Check for null values in the 'date' column
        if df['date'].isnull().sum() > 0:
            raise ValueError("Input DataFrame contains null values in 'date' column")

        # Convert the 'date' column to datetime format
        df['date'] = pd.to_datetime(df['date'])

        # Print some information about the cleaned DataFrame
        print(df.head(2))
        print(f"Columns: {df.dtypes}")
        print(f"Number of rows: {len(df)}")

        # Return the cleaned DataFrame
        return df

    except ValueError as e:
        # Log the error message and raise the exception
        print(f"Error cleaning DataFrame: {e}")
        raise


@task(log_prints=True)
def write_local(df_transformed: pd.DataFrame) -> Path:
    """
    Writes a DataFrame as a compressed Parquet file to the local disk.

    Args:
        df_transformed (pd.DataFrame): The DataFrame to be written as a Parquet file.

    Returns:
        Path: The path to the written Parquet file.
    """
    # Define the path to the output Parquet file
    parquet_path = Path("data/owid-covid-data.parquet")

    # Write the DataFrame to the output Parquet file with gzip compression
    df_transformed.to_parquet(parquet_path, compression="gzip")

    # Return the path to the written Parquet file
    return parquet_path

@task(log_prints=True)
def write_gcs(parquet_path: Path) -> None:
    """Upload local parquet file into GCS Bucket"""
    gcp_cloud_storage_bucket_block = GcsBucket.load("googlecloud-connector")
    gcp_cloud_storage_bucket_block.upload_from_path(from_path=parquet_path, to_path=parquet_path)
    return


@task(log_prints=True)
def extract_from_gcs(parquet_path: Path) -> Path:
    """Download data from GCS"""
    gcp_cloud_storage_bucket_block = GcsBucket.load("googlecloud-connector")
    gcp_cloud_storage_bucket_block.get_directory(from_path=parquet_path, local_path=f"data/")
    return Path(f"{parquet_path}")


@task(log_prints=True)
def write_bq(path: Path) -> None:
    """Read parquet file and write dataframe to BigQuery"""
    df_final = pd.read_parquet(path)
    gcp_credentials_block = GcpCredentials.load("gcs-connector")

    df_final.to_gbq(
        destination_table="github_archive_de.covid_bqdata",
        project_id="github-archive-de",
        credentials=gcp_credentials_block.get_credentials_from_service_account(),
        chunksize=500_000,
        if_exists="replace",
    )

    return

@flow(name="Ingest Data")
def main_flow(table_name: str = "Covid") -> None:
    """Main ETL flow to ingest data"""
    
    raw_data = extract_data()
    df_transformed = transform_data(raw_data)
    parquet_path = write_local(df_transformed)

    write_gcs(parquet_path)
    path = extract_from_gcs(parquet_path)
    write_bq(path)

if __name__ == "__main__":
    main_flow()
    



#prefect deployment build web_to_gcs.py:etl_web_to_gcs -n 'covid_data_to_bucket' --cron "0 5 * * *" -a # creates deployment yaml file and schedule it via CRON daily at 6 CET 