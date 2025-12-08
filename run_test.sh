#!/usr/bin/env bash
set -euo pipefail

# create .venv and install
if [ -d .venv ]; then
  echo "Removing existing .venv"
  rm -rf .venv
fi
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

# run tests
mkdir -p logs
python -u -m pytest tests -q | tee logs/test_run.log
