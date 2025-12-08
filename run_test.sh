#!/bin/bash

# run_test.sh - Test runner script for Linux/macOS

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_PATH="$SCRIPT_DIR/.venv"
LOG_DIR="$SCRIPT_DIR/logs"
LOG_FILE="$LOG_DIR/test_run.log"

echo "Running tests on Linux/macOS..."

# Check if .venv exists
if [ ! -d "$VENV_PATH" ]; then
    echo "Error: Virtual environment not found at $VENV_PATH"
    echo "Please run setup.sh first"
    exit 1
fi

# Create logs directory
mkdir -p "$LOG_DIR"

# Activate virtual environment
source "$VENV_PATH/bin/activate"

# Log environment information
{
    echo "========================================" 
    echo "Test Run - $(date)"
    echo "========================================"
    echo "Environment Name: .venv"
    echo "Environment Path: $VENV_PATH"
    echo "Python Version: $(python --version)"
    echo "Pip Version: $(pip --version)"
    echo "========================================"
    echo ""
} | tee "$LOG_FILE"

# Run all test files
cd "$SCRIPT_DIR"
for test_file in tests/*.py; do
    if [ -f "$test_file" ]; then
        echo "Running $test_file..." | tee -a "$LOG_FILE"
        python "$test_file" 2>&1 | tee -a "$LOG_FILE" || true
        echo "" >> "$LOG_FILE"
    fi
done

echo "Tests completed! Results saved to $LOG_FILE"
