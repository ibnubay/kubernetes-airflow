from datetime import datetime
import logging
from airflow import DAG
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import kubernetes.client.models as k8s

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

# init_container = k8s.V1Container(
#   name="init-container",
#   image="ubuntu:18.04",
#   image_pull_policy='IfNotPresent',
#   # env=init_environments,
#   # volume_mounts=init_container_volume_mounts,
#   command=["bash", "-cx"],
#   args=["echo 10"]
# )

for x in range(10):
    t2 = BashOperator(
        task_id=f'sleep_{x}',
        depends_on_past=False,
        bash_command='sleep 10',
        retries=0,
        dag=main_dag,
        executor_config={"KubernetesExecutor": {"image": "airflow_kube_minimum:1.10.10",
                                                "image_pull_policy": "Never",
                                                # "request_memory": "10Mi",
                                                # "limit_memory": "128Mi"
                                                }
                         },
    )

# def print_stuff():
#     print("AAAAAAA")

# start_task = PythonOperator(
#     task_id="start_task", python_callable=print_stuff, dag=main_dag,
#     retries=0,
#     # executor_config={"KubernetesExecutor": {"labels": {"foo": "bar"}}}
#     executor_config={"KubernetesExecutor": {"image": "airflow_kube_minimum:1.10.10",
#                                             "image_pull_policy": "Never",
#     #                                         # "request_memory": "10Mi",
#     #                                         # "limit_memory": "128Mi",
#                                             }},
#     #                  },
# )



# passing = KubernetesPodOperator(namespace='airflow',
#                                 # image="ubuntu:18.04",
#                                 # cmds=["bash", "-cx"],
#                                 # arguments=["echo", "10", "echo pwd"],
#                                 image="10.152.183.54:32000/airflow_kube:1.10.10",
#                                 image_pull_policy='IfNotPresent',
#                                 cmds=["sleep 5"],
#                                 # cmds=["Python","-c"],
#                                 # arguments=["print('hello world')"],
#                                 # labels={"foo": "bar"},
#                                 name="passing-test",
#                                 task_id="passing-task",
#                                 is_delete_operator_pod=True,
#                                 dag=main_dag,
#                                 in_cluster=True
#                                 )