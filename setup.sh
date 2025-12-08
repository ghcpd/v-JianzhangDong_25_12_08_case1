#!/bin/bash
set -e
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
# Install dependencies
pip install --prefer-binary --no-cache-dir -r requirements.txt
echo "Environment setup complete. Activate with: source .venv/bin/activate"
