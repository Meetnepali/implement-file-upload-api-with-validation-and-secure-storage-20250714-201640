#!/bin/bash
set -e
bash install.sh
source .venv/bin/activate
echo 'Starting FastAPI application...'
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
