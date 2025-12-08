# Project environment and test automation

This repository includes generated files to make dependency maintenance and testing reproducible.

Files generated:
- requirements_backup.txt: a copy of the original requirements before updates.
- requirements.txt: updated, secure, and pinned dependency versions.
- report.json: a simplified report listing packages that were updated and reasons.
- Dockerfile: Dockerfile to build a containerized environment and run tests.
- setup.sh: script to set up the .venv and install dependencies (Linux/macOS).
- run_test.sh: script to setup .venv and run tests, storing results in logs/test_run.log (Linux/macOS).
- run_test.bat: equivalent for Windows.
- auto_test.py: Python script to create a fresh .venv, install dependencies, run tests and append environment info to README.md.
- .gitignore: ignores .venv and logs.

Setup

Linux / macOS:
1. Make the scripts executable: chmod +x setup.sh run_test.sh
2. Run `./setup.sh` to create a fresh .venv and install dependencies.
3. Run tests with `./run_test.sh`.

Windows (PowerShell / CMD):
1. Run `python -m venv .venv` (if you prefer manual creation).
2. Run `.


















- Test logs: logs/test_run.logLogs2. Run `python auto_test.py` — it will create a fresh .venv, install dependencies and run tests. Results are appended to README.md and written to logs/test_run.log.1. Ensure Python 3.10+ is available on PATH.Using auto_test.py  docker run --rm project-testRun:  docker build -t project-test .Build:Using Dockerun_test.bat` to create .venv, install dependencies and run tests.
Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_08_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_08_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\projects\v-JianzhangDong_25_12_08_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)

Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_08_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_08_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\projects\v-JianzhangDong_25_12_08_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)

Environment: .venv
Path: D:\projects\v-JianzhangDong_25_12_08_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_08_case1\.venv
Python: Python 3.14.0
Pip: pip 25.3 from D:\projects\v-JianzhangDong_25_12_08_case1\oswe-mini-m22a3s400\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)
