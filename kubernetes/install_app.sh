#!/usr/bin/env bash
microk8s kubectl apply -f airflow-namespace.yaml
microk8s kubectl apply -f airflow-redis-deployment.yaml
microk8s kubectl apply -f airflow-redis-service.yaml
microk8s kubectl apply -f airflow-postgres-deployment.yaml
microk8s kubectl apply -f airflow-postgres-service.yaml
microk8s kubectl apply -f airflow-webserver-deployment.yaml
microk8s kubectl apply -f airflow-webserver-service.yaml
microk8s kubectl apply -f airflow-scheduler-deployment.yaml
microk8s kubectl apply -f airflow-worker-deployment.yaml
microk8s kubectl apply -f airflow-worker-service.yaml
microk8s kubectl apply -f airflow-flower-deployment.yaml
microk8s kubectl apply -f airflow-flower-service.yaml
microk8s kubectl apply -f airflow-ingress.yaml