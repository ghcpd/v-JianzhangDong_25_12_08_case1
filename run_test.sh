#!/usr/bin/env bash
set -euo pipefail

if [ ! -d ".venv" ]; then
  echo ".venv not found. Run setup.sh first to create it."
  exit 1
fi

source .venv/bin/activate
mkdir -p logs
LOGFILE=logs/test_run.log
echo "Running tests at $(date)" > "$LOGFILE"
for f in tests/*.py; do
  echo "---- Running $f ----" | tee -a "$LOGFILE"
  python "$f" 2>&1 | tee -a "$LOGFILE"
  echo "Exit code: $?" >> "$LOGFILE"
done

echo "Tests complete. See $LOGFILE"
