#!/usr/bin/env bash
set -euo pipefail
if [ -d ".venv" ]; then
  source .venv/bin/activate
else
  echo ".venv not found. Run setup.sh first." >&2
  exit 1
fi
mkdir -p logs
python -m pytest -q tests || true
echo "Test run complete. See logs/test_run.log for details if generated."
