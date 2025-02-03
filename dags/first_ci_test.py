# dags/example_airflow_dag.py

from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2023, 1, 1)
}

# Define the DAG
with DAG(
    'example_airflow_dag_from_cis',  # Distinctive DAG name
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # A simple task that prints the current date
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    print_date
