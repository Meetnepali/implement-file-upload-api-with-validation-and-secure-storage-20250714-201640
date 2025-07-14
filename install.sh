#!/bin/bash
set -e

# Install system dependencies
if ! command -v python3 &> /dev/null; then
  echo 'python3 not found, installing...'
  apt-get update && apt-get install -y python3 python3-venv python3-pip
fi
if ! command -v pip3 &> /dev/null; then
  echo 'pip3 not found, installing...'
  apt-get update && apt-get install -y python3-pip
fi

# Ensure pip is up to date
python3 -m pip install --upgrade pip

# (Re)create virtual environment if not exists or incompatible
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi
source .venv/bin/activate

pip install -r requirements.txt
