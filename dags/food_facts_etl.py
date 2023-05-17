import pandas as pd

# Define file paths
tsv_file_path = '/opt/airflow/dags/Data/en.openfoodfacts.org.products.tsv'
csv_file_path = '/opt/airflow/dags/Data/food_facts.csv'

# Read the TSV file into a pandas DataFrame
df = pd.read_csv(tsv_file_path, sep='\t')

# Convert the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"TSV file converted to CSV: {csv_file_path}")
