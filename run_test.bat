@echo off
IF NOT EXIST .venv\Scripts\activate.bat (
  echo .venv not found. Run setup.sh or create a virtual environment first.
  exit /b 1
)
call .venv\Scripts\activate.bat
if not exist logs mkdir logs
set LOGFILE=logs\test_run.log
echo Running tests at %DATE% %TIME% > %LOGFILE%
for %%f in (tests\*.py) do (
  echo ---- Running %%f ---- >> %LOGFILE%
  python %%f >> %LOGFILE% 2>&1
  echo Exit code: %ERRORLEVEL% >> %LOGFILE%
)
echo Tests complete. See %LOGFILE%
