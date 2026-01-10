#!/bin/bash

# setup.sh - Environment setup script for Linux/macOS

set -e

echo "Setting up Python environment for Linux/macOS..."

# Check if Python 3.14 is available
if ! command -v python3.14 &> /dev/null; then
    echo "Warning: Python 3.14 not found. Using available Python version."
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python3.14"
fi

echo "Python version: $($PYTHON_CMD --version)"
echo "Pip version: $($PYTHON_CMD -m pip --version)"

# Remove existing .venv if present
if [ -d ".venv" ]; then
    echo "Removing existing .venv directory..."
    rm -rf .venv
fi

# Create virtual environment
echo "Creating virtual environment..."
$PYTHON_CMD -m venv .venv

# Activate virtual environment
echo "Activating virtual environment..."
source .venv/bin/activate

# Upgrade pip
echo "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
echo "Installing dependencies from requirements.txt..."
pip install -r requirements.txt

# Create logs directory
mkdir -p logs

# Display environment info
echo ""
echo "========================================"
echo "Environment setup completed!"
echo "========================================"
echo "Python: $($PYTHON_CMD --version)"
echo "Pip: $(pip --version)"
echo "Virtual environment: $(pwd)/.venv"
echo "To activate: source .venv/bin/activate"
echo "========================================"
