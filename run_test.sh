#!/bin/bash
set -e
if [ -d ".venv" ]; then
  echo "Using .venv"
  source .venv/bin/activate
  PY=.venv/bin/python
else
  echo ".venv not found; using system python"
  PY=python
fi
mkdir -p logs
$PY -u tests/case_1.py | tee logs/case_1.log
$PY -u tests/case_2.py | tee logs/case_2.log
$PY -u tests/case_3.py | tee logs/case_3.log
echo "All tests executed. Logs under logs/"
