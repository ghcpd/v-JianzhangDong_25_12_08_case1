@echo off
if not exist .venv\Scripts\python.exe (
  echo .venv not found. Run setup.sh or create virtual environment first.
  exit /b 1
)
.venv\Scripts\python -m pytest -q tests || echo Test run completed with errors
