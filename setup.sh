#!/usr/bin/env bash
set -euo pipefail

echo "Creating a new .venv and installing requirements..."
if [ -d .venv ]; then
  echo "Removing existing .venv..."
  rm -rf .venv
fi

python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
pip install --no-cache-dir -r requirements.txt

echo "Environment ready in .venv/"
