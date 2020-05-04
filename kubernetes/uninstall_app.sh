#!/usr/bin/env bash
microk8s kubectl delete -f airflow-redis-deployment.yaml
microk8s kubectl delete -f airflow-redis-service.yaml
microk8s kubectl delete -f airflow-postgres-deployment.yaml
microk8s kubectl delete -f airflow-postgres-service.yaml
microk8s kubectl delete -f airflow-webserver-deployment.yaml
microk8s kubectl delete -f airflow-webserver-service.yaml
microk8s kubectl delete -f airflow-scheduler-deployment.yaml
microk8s kubectl delete -f airflow-worker-deployment.yaml
microk8s kubectl delete -f airflow-worker-service.yaml
microk8s kubectl delete -f airflow-flower-deployment.yaml
microk8s kubectl delete -f airflow-flower-service.yaml
microk8s kubectl delete -f airflow-ingress.yaml
microk8s kubectl delete -f airflow-namespace.yaml