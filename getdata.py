import os
import random
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Directory to save the downloaded CSV files
DOWNLOAD_FOLDER = "datasets"

# Function to download only CSV files from a dataset
def download_csv_files(dataset_ref):
    try:
        file = api.dataset_list_files(dataset_ref)
        for x in file:
            if x.endswith(".csv"):
                api.dataset_download_file(dataset_ref, x, path="datasets")
        print('done')
        # Look for CSV files in the downloaded dataset
    except Exception as e:
        print(f"Failed to download {dataset_ref}: {e}")

# Function to fetch random datasets and filter for CSV files
def download_random_csv_datasets(num_datasets=1000):
    datasets = api.dataset_list(search="dataset")
    
    for x in range(num_datasets):
        download_csv_files(datasets[x].ref)

# Call the function to download 1000 random CSV files from datasets
download_random_csv_datasets(1000)
