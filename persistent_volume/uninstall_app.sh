#!/usr/bin/env bash
NAMESPACE=$1

microk8s kubectl delete -f app-postgresql.yaml --namespace=${NAMESPACE}
microk8s kubectl delete -f app-minio.yaml --namespace=${NAMESPACE}
microk8s kubectl delete -f app-airflow.yaml --namespace=${NAMESPACE}
microk8s kubectl delete -f app-ingress.yaml --namespace=${NAMESPACE}
microk8s kubectl delete -f app-volume.yaml --namespace=${NAMESPACE}
microk8s kubectl delete namespace ${NAMESPACE} || true