@echo off
if exist .venv (
  echo .venv exists
) else (
  echo Creating virtual environment .venv
  python -m venv .venv
  .venv\Scripts\python -m pip install --upgrade pip setuptools wheel
  .venv\Scripts\pip install --no-cache-dir -r requirements.txt
)

if not exist logs mkdir logs
.venv\Scripts\pytest -q > logs\test_run.log 2>&1
type logs\test_run.log
echo Tests completed - output written to logs\test_run.log
