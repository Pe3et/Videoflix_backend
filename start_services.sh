#!/bin/bash

source env/bin/activate

# Start Django development server
bash -c "python3 manage.py runserver; exec bash" &

# Start Redis server
bash -c "redis-server; exec bash" &

# Start Celery worker
bash -c "celery -A Videoflix_Backend.celery worker --loglevel=info; exec bash"
