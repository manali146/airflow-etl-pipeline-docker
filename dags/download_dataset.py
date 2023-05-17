import os
os.environ['KAGGLE_CONFIG_DIR'] = '/opt/airflow/.kaggle'
import kaggle

# Set your Kaggle API credentials
os.environ['KAGGLE_USERNAME'] = 'manalithakur'
os.environ['KAGGLE_KEY'] = '3ded1d7d880ed736cb0de2b98c168093'

# Define the dataset name and destination directory
dataset_name = 'openfoodfacts/world-food-facts'
destination_dir = './dags/Data'

def download_dataset(dataset_name, destination_dir):
    """
    Downloads the Open Food Facts dataset from Kaggle.

    Args:
        dataset_name (str): Name of the dataset on Kaggle.
        destination_dir (str): Directory to save the downloaded dataset.

    Returns:
        None
    """

    # Download the dataset from Kaggle
    kaggle.api.dataset_download_files(dataset_name, path=destination_dir, unzip=True)

    # List the downloaded files
    files = os.listdir(destination_dir)
    print("Downloaded files:")
    for file in files:
        print(file)

if __name__ == '__main__':
    # Run the download_dataset function
    download_dataset(dataset_name, destination_dir)
