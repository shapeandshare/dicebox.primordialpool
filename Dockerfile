# FROM tensorflow/tensorflow:latest-gpu
# FROM tensorflow/tensorflow
FROM python:2.7

WORKDIR /app

COPY ./app /app
COPY ./dicebox/dicebox /app/dicebox
COPY ./dicebox/dicebox.config /app

RUN pip install -r requirements.txt \
    && useradd -M -U -u 1000 primordialpool \
    && chown -R primordialpool /app

ENTRYPOINT ["python", "./primordialpool.py"]

