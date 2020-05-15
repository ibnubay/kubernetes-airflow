#!/usr/bin/env bash
NAMESPACE=$1

microk8s kubectl create namespace ${NAMESPACE} || true
microk8s kubectl apply -f app-volume.yaml --namespace=${NAMESPACE}
microk8s kubectl apply -f app-postgresql.yaml --namespace=${NAMESPACE}
microk8s kubectl apply -f app-minio.yaml --namespace=${NAMESPACE}
microk8s kubectl apply -f app-airflow.yaml --namespace=${NAMESPACE}
microk8s kubectl apply -f app-ingress.yaml --namespace=${NAMESPACE}