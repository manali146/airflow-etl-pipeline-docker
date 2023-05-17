# import libraries
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
# from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago
from datetime import timedelta
import pandas as pd

def transform_data(input_file, output_file):
    # This function should read the downloaded data, apply transformations, and save the transformed data

    # Read the downloaded CSV file
    facts_data = pd.read_csv(input_file)
    
    # Perform data transformations
    # Get the column names with no values
    empty_columns = facts_data.columns[facts_data.isnull().all()]
    facts_data.drop(columns = empty_columns, inplace = True)
    
    facts_data.drop_duplicates(subset=['code'],inplace=True)
    facts_data.drop(columns = ['created_t','last_modified_t'],inplace=True)
    facts_data = facts_data[['code', 'product_name', 'quantity', 'packaging', 'brands', 'categories', 'countries', 'serving_size', 'nutrition_grade_fr', 'nutrition-score-uk_100g']]    # Save the transformed data
    facts_data.to_csv(output_file, index=False)

# defining DAG arguments
default_args = {
    'owner' : 'Manali Thakur',
    'start_date' : days_ago(0),
    'email' : ['manalithakur165@gmail.com'],
    'email_on_retry' : 'True',
    'email_on_failure' : 'True',
    'retries' : 0,
    'retry_delay' : timedelta(minutes = 2),
}

# defining the DAG
dag = DAG(
    'food_facts_etl_pipeline',
    default_args = default_args,
    description = 'ETL pipeline for Open Food Facts dataset',
    schedule_interval = timedelta(days = 1),
)

# defining tasks
extract_data_task = BashOperator(
    task_id = 'extract_data',
    bash_command = 'python /opt/airflow/dags/food_facts_etl.py',
    dag = dag,
)

transform_and_load_data_task = PythonOperator(
    task_id = 'transform_data',
    python_callable = transform_data,
    op_args = ['/opt/airflow/dags/Data/food_facts.csv','/opt/airflow/dags/Data/transformed_food_facts.csv'],
    dag = dag,
)

# defining pipeline
extract_data_task >> transform_and_load_data_task