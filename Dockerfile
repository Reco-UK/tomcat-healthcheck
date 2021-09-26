FROM python:3.9-slim

ENV PYTHONUNBUFFERED True
ENV PORT 8888
ENV WORKERS 1
ENV THREADS 8
ENV TIMEOUT 0
ENV TOMCAT_MGR_URL http://192.168.1.127:8080/manager

WORKDIR /agent

COPY requirements.txt .
COPY main.py .

RUN python3 -m venv venv && \
    . venv/bin/activate && \
    venv/bin/python3 -m pip install --upgrade pip && \
    pip3 install -r requirements.txt;

EXPOSE $PORT

CMD . venv/bin/activate && exec gunicorn --bind :$PORT --workers $WORKERS --threads $THREADS --timeout $TIMEOUT main:app