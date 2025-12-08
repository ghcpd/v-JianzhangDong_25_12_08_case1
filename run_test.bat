@echo off
REM remove existing .venv
if exist .venv ( rmdir /s /q .venv )
python -m venv .venv
.venv\Scripts\pip.exe install --upgrade pip setuptools wheel
.venv\Scripts\pip.exe install -r requirements.txt

if not exist logs mkdir logs
.venv\Scripts\pytest.exe tests -q > logs\test_run.log 2>&1
type logs\test_run.log
