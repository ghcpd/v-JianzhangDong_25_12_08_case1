#!/usr/bin/env bash
set -euo pipefail

# Create a fresh virtual environment under .venv
if [ -d ".venv" ]; then
  echo "Removing existing .venv/"
  rm -rf .venv
fi
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt

echo "Environment setup complete. Activate with: source .venv/bin/activate"
