from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount
from datetime import datetime

DBT_PATH = "C:/Users/Khairi/Desktop/Data_Engineer/ecommerce_data_pipeline/dbt"
DAGS_PATH = "C:/Users/Khairi/Desktop/Data_Engineer/ecommerce_data_pipeline/dags"

with DAG(
    dag_id="order_monitoring_dag",
    start_date=datetime(2026, 2, 26),
    schedule=None,
    catchup=False,
) as dag:

    run_dbt = DockerOperator(
        task_id="run_dbt_models",
        image="ghcr.io/dbt-labs/dbt-snowflake:latest",
        command="run --project-dir /usr/app",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mounts=[
            Mount(
                source="C:/Users/Khairi/Desktop/Data_Engineer/ecommerce_data_pipeline/dbt",
                target="/usr/app",
                type="bind"
            ),
        ],
        working_dir="/usr/app",
        auto_remove=True,
        mount_tmp_dir=False,
    )

    check_orders = DockerOperator(
        task_id="check_delayed_orders",
        image="ecommerce-python",
        command="python /app/dags/utils/check_delayed_orders.py",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        auto_remove=True,
        mount_tmp_dir=False,

        mounts=[
            Mount(
                source="C:/Users/Khairi/Desktop/Data_Engineer/ecommerce_data_pipeline",
                target="/app",
                type="bind"
            )
        ]
    )
    run_dbt >> check_orders