#!/bin/bash

PYTHONUNBUFFERED=True
NAME=agent
PORT=8888
WORKERS=1
THREADS=8
TIMEOUT=0

python3 -m venv venv && \
. venv/bin/activate && \
venv/bin/python3 -m pip --quiet install --upgrade pip && \
    pip3 --quiet install -r ./requirements.txt;

. venv/bin/activate && exec gunicorn main:app --name $NAME --bind :$PORT --workers $WORKERS --threads $THREADS --timeout $TIMEOUT