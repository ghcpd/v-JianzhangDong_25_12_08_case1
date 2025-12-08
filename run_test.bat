@echo off
REM run_test.bat - Test runner script for Windows

setlocal enabledelayedexpansion

set SCRIPT_DIR=%~dp0
set VENV_PATH=%SCRIPT_DIR%.venv
set LOG_DIR=%SCRIPT_DIR%logs
set LOG_FILE=%LOG_DIR%\test_run.log

echo Running tests on Windows...

REM Check if .venv exists
if not exist "%VENV_PATH%" (
    echo Error: Virtual environment not found at %VENV_PATH%
    echo Please run setup.bat first
    exit /b 1
)

REM Create logs directory
if not exist "%LOG_DIR%" (
    mkdir "%LOG_DIR%"
)

REM Activate virtual environment
call "%VENV_PATH%\Scripts\activate.bat"

REM Log environment information
(
    echo ========================================
    echo Test Run - %date% %time%
    echo ========================================
    echo Environment Name: .venv
    echo Environment Path: %VENV_PATH%
    for /f "tokens=*" %%a in ('python --version') do echo Python Version: %%a
    for /f "tokens=*" %%a in ('pip --version') do echo Pip Version: %%a
    echo ========================================
    echo.
) > "%LOG_FILE%"

REM Run all test files
cd /d "%SCRIPT_DIR%"
for %%f in (tests\*.py) do (
    echo Running %%f... >> "%LOG_FILE%"
    python "%%f" >> "%LOG_FILE%" 2>&1
    echo. >> "%LOG_FILE%"
)

echo Tests completed! Results saved to %LOG_FILE%
