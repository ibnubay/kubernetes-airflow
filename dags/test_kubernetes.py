from datetime import datetime
import logging
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator

logger = logging.getLogger(__name__)
data_team_args = {
    "owner": "your_project",
    "depends_on_past": False,
    "start_date": datetime(2020, 5, 1),
    # "email": ["your@mail.com"],
    "backfill": False
}

main_dag = DAG(dag_id="kubernetes_dag", description="Kubernetes Dag"
               , schedule_interval=None, catchup=False, default_args=data_team_args)

for x in range(10):
    t2 = BashOperator(
        task_id=f'sleep_{x}',
        depends_on_past=False,
        bash_command='sleep 20',
        retries=0,
        dag=main_dag,
        # executor_config={"KubernetesExecutor": {"image": "airflow_kube_minimum:1.10.10",
        #                                         "image_pull_policy": "Never",
        #                                         # "request_memory": "10Mi",
        #                                         # "limit_memory": "128Mi"
        #                                         }
        #                  },
    )


def sample_dag():
    try:
        a = [1, 2, 3]
        logging.info(a)

    except Exception as error:
        logging.error(error)


sample_dag = PythonOperator(
    task_id="sample_dag"
    , default_args=data_team_args
    , python_callable=sample_dag
    , dag=main_dag
)
