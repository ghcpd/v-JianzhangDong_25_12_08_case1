#!/usr/bin/env bash
set -euo pipefail

if [ ! -d .venv ]; then
  echo ".venv not found — calling setup.sh to create one..."
  ./setup.sh
fi

source .venv/bin/activate

mkdir -p logs
echo "Running tests with pytest and writing output to logs/test_run.log"
pytest -q | tee logs/test_run.log

echo "Tests completed — see logs/test_run.log for details."
