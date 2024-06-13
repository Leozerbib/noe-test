from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import subprocess

def run_script(script_path):
    result = subprocess.run(["python3", script_path], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)

with DAG(
    'dagAirflow',
    default_args={
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(seconds=15),
    },
    description='A DAG to fetch and save movie data',
    schedule=None,  # Remplacez schedule_interval par schedule
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    fetch_data_1 = PythonOperator(
        task_id='fetch_countries',
        python_callable=run_script,
        op_kwargs={'script_path': 'C:\Users\leo\OneDrive - ISEP\Bureau\taffe\test\noe test\controler.py'},
    )

    fetch_data_2 = PythonOperator(
        task_id='fetch_languages',
        python_callable=run_script,
        op_kwargs={'script_path': '/path/to/your/directory/fetch_data_2.py'},
    )

    fetch_data_1
    fetch_data_2