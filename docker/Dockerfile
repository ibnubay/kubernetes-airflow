# Base Image
FROM bitnami/python:3.7-prod

ARG AIRFLOW_USER=airflow
ARG AIRFLOW_GROUP=datawarehouse

ENV AIRFLOW_USER=${AIRFLOW_USER}
ENV AIRFLOW_GROUP=${AIRFLOW_GROUP}

RUN addgroup ${AIRFLOW_GROUP} && adduser --system --no-create-home ${AIRFLOW_USER} \
    && adduser ${AIRFLOW_USER} ${AIRFLOW_GROUP}
# End of Base Image

ARG VERSION="1.10.10"
# Default
ARG SUBMODULES="async,crypto,celery,postgres,jdbc,redis,statsd"

ENV AIRFLOW_MODULE="apache-airflow[${SUBMODULES}]==${VERSION}"
ENV AIRFLOW_HOME="/app/airflow"
ENV AIRFLOW_CONFIG="/app/airflow.cfg"

WORKDIR ${AIRFLOW_HOME}
# Install packages
ENV buildDeps='libffi-dev g++'

COPY entrypoint /entrypoint
COPY airflow.cfg /app/airflow.cfg
COPY dags/sample_dag.py /app/airflow/dags/sample_dag.py

RUN set -ex \
    && buildDeps='libffi-dev g++ build-essential' \
    && apt-get update -yqq \
    && apt-get install -yqq --no-install-recommends \
        $buildDeps \
        locales \
        apt-utils \
        netcat \
        cron \
        git \
        patch \
    && sed -i 's/^# en_US.UTF-8 UTF-8$/en_US.UTF-8 UTF-8/g' /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 \
    && rm -r /var/lib/apt/lists /var/cache/apt/archives

RUN pip install --no-cache-dir -U setuptools \
    && pip install --no-cache-dir -U pip wheel certifi gitdb \
    && pip install --no-cache-dir "${AIRFLOW_MODULE}"

RUN apt-get purge --auto-remove -yqq $buildDeps \
    && apt-get autoremove -yqq --purge \
    && apt-get clean

RUN chmod +x /entrypoint \
    && chown -R ${AIRFLOW_USER}:${AIRFLOW_GROUP} ${AIRFLOW_HOME}

USER ${AIRFLOW_USER}

# Expose all airflow ports
EXPOSE 8080 5555 8793

# Run airflow
ENTRYPOINT ["/entrypoint"]