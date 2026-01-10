#!/usr/bin/env python
"""
auto_test.py - Automatic environment detection and test runner

This script automatically detects the Python environment, activates it,
and runs all test files from the tests/ directory. Results are logged
to logs/test_run.log.
"""

import os
import sys
import subprocess
import platform
from pathlib import Path
from datetime import datetime


# Add project root to Python path so app modules can be imported
sys.path.insert(0, str(Path(__file__).parent.resolve()))


def get_venv_path():
    """Get the path to the virtual environment."""
    script_dir = Path(__file__).parent.resolve()
    venv_path = script_dir / ".venv"
    return venv_path


def get_python_executable():
    """Get the Python executable from the virtual environment."""
    venv_path = get_venv_path()
    
    if not venv_path.exists():
        print(f"Error: Virtual environment not found at {venv_path}")
        print("Please run setup.sh (Linux/macOS) or setup.bat (Windows) first.")
        sys.exit(1)
    
    if platform.system() == "Windows":
        python_exe = venv_path / "Scripts" / "python.exe"
    else:
        python_exe = venv_path / "bin" / "python"
    
    if not python_exe.exists():
        print(f"Error: Python executable not found at {python_exe}")
        sys.exit(1)
    
    return python_exe


def create_logs_directory():
    """Create logs directory if it doesn't exist."""
    logs_dir = Path(__file__).parent / "logs"
    logs_dir.mkdir(exist_ok=True)
    return logs_dir / "test_run.log"


def run_tests():
    """Run all test files and log results."""
    script_dir = Path(__file__).parent.resolve()
    tests_dir = script_dir / "tests"
    log_file = create_logs_directory()
    
    # Get environment info
    venv_path = get_venv_path()
    python_exe = get_python_executable()
    
    # Get Python and pip versions
    try:
        python_version = subprocess.check_output(
            [str(python_exe), "--version"], 
            text=True
        ).strip()
    except subprocess.CalledProcessError:
        python_version = "Unknown"
    
    try:
        pip_version = subprocess.check_output(
            [str(python_exe), "-m", "pip", "--version"], 
            text=True
        ).strip()
    except subprocess.CalledProcessError:
        pip_version = "Unknown"
    
    # Open log file and write header
    with open(log_file, "w") as f:
        f.write("=" * 60 + "\n")
        f.write(f"Test Run - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n")
        f.write(f"Environment Name: .venv\n")
        f.write(f"Environment Path: {venv_path.resolve()}\n")
        f.write(f"Python Version: {python_version}\n")
        f.write(f"Pip Version: {pip_version}\n")
        f.write(f"Operating System: {platform.system()} {platform.release()}\n")
        f.write("=" * 60 + "\n\n")
    
    # Print header to console
    print("=" * 60)
    print(f"Test Run - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print(f"Environment Name: .venv")
    print(f"Environment Path: {venv_path.resolve()}")
    print(f"Python Version: {python_version}")
    print(f"Pip Version: {pip_version}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print("=" * 60)
    print()
    
    # Find and run all test files
    test_files = sorted(tests_dir.glob("*.py"))
    
    if not test_files:
        print("No test files found in tests/ directory.")
        with open(log_file, "a") as f:
            f.write("No test files found in tests/ directory.\n")
        return
    
    print(f"Found {len(test_files)} test file(s) to run.\n")
    
    for test_file in test_files:
        print(f"Running {test_file.name}...")
        print("-" * 60)
        
        with open(log_file, "a") as f:
            f.write(f"Running {test_file.name}...\n")
            f.write("-" * 60 + "\n")
        
        try:
            result = subprocess.run(
                [str(python_exe), str(test_file)],
                cwd=str(script_dir),
                capture_output=True,
                text=True,
                timeout=300,
                env={**os.environ, 'PYTHONPATH': str(script_dir)}
            )
            
            # Write output to log and console
            output = result.stdout + result.stderr
            print(output)
            
            with open(log_file, "a") as f:
                f.write(output)
                if result.returncode != 0:
                    f.write(f"\nTest failed with exit code: {result.returncode}\n")
                f.write("\n")
            
        except subprocess.TimeoutExpired:
            error_msg = f"Test {test_file.name} timed out after 300 seconds.\n"
            print(error_msg)
            with open(log_file, "a") as f:
                f.write(error_msg)
        except Exception as e:
            error_msg = f"Error running {test_file.name}: {str(e)}\n"
            print(error_msg)
            with open(log_file, "a") as f:
                f.write(error_msg)
        
        print()
    
    # Write footer
    footer = "\n" + "=" * 60 + "\n"
    footer += f"Test run completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
    footer += "=" * 60 + "\n"
    
    print(footer)
    with open(log_file, "a") as f:
        f.write(footer)
    
    print(f"Results saved to: {log_file}")


if __name__ == "__main__":
    run_tests()
