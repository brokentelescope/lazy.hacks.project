import os
import random
from kaggle.api.kaggle_api_extended import KaggleApi

# Initialize the Kaggle API
api = KaggleApi()
api.authenticate()

# Directory to save the downloaded CSV files
DOWNLOAD_FOLDER = "datasets"

# Function to download only CSV files from a dataset
def download_csv_files(dataset):
    file = api.dataset_list_files(dataset.ref)
    print(file)
    for x in file.files:
        if x.endswith(".csv"):
            api.dataset_download_file(dataset.ref, x, path="datasets")
    print('done')
#except Exception as e:
 #   print(f"Failed to download {dataset.ref}: {e}")

# Function to fetch random datasets and filter for CSV files
def download_random_csv_datasets():
    datasets = api.dataset_list(search="dataset")
    print(datasets)
    n = len(datasets)
    for x in range(1):
        download_csv_files(datasets[x])

download_random_csv_datasets()
