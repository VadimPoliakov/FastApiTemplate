#!/bin/bash

alembic upgrade head

uvicorn src.main:app --host 0.0.0.0 --port 8000 --log-level=info --forwarded-allow-ips='*' --proxy-headers
#gunicorn app.main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind=0.0.0.0:8000 --timeout 10000 --log-level=info --access-logfile - --error-logfile -
