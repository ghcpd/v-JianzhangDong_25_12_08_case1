Project test & environment helper files

Generated files and purpose:
- requirements_backup.txt: A backup of the original requirements.txt before updates.
- requirements.txt: Updated, pinned dependency versions (safe/stable versions chosen for Python 3.14).
- report.json: Simplified report listing updated packages and reasons for changes.
- Dockerfile: A reproducible Docker image that installs the pinned requirements.
- setup.sh: Creates a fresh .venv virtual environment and installs dependencies (Linux/macOS).
- run_test.sh: Runs all tests in tests/*.py using the .venv environment and logs output to logs/test_run.log (Linux/macOS).
- run_test.bat: Same as run_test.sh but for Windows.
- auto_test.py: Locates .venv's Python interpreter, runs all tests in tests/, writes logs to logs/test_run.log, and appends environment info to this README.md.
- .gitignore: Ignores .venv/ and logs/.
- logs/: Directory where test outputs are stored.

Setup instructions (Linux/macOS):
1. Ensure Python 3.14 is installed on your machine.
2. Run: bash setup.sh
3. Activate: source .venv/bin/activate

Setup instructions (Windows):
1. Ensure Python 3.14 is installed.
2. Create and activate a venv: python -m venv .venv
3. Activate: .venv\Scripts\activate.bat
4. Install dependencies: python -m pip install --upgrade pip setuptools wheel && pip install -r requirements.txt

Running tests:
- Linux/macOS: After activation, run ./run_test.sh
- Windows: After activation, run run_test.bat
- Or run python auto_test.py which will detect .venv, run tests, log results to logs/test_run.log, and append environment info to this README.md.

Checking logs:
- Open logs/test_run.log to view test outputs and exit codes.

Notes:
- Do not commit .venv/ or logs/ (added to .gitignore).
- If .venv/ already exists and you want a fresh environment, delete it and re-run setup.sh.

Last created venv environment details:
- Environment: .venv
- Absolute path: D:\projects\v-JianzhangDong_25_12_08_case1\vsc-5mini-mix22-arm5-s270\v-JianzhangDong_25_12_08_case1\.venv
- Python: Python 3.14.0
- pip: pip 25.3


## Last auto_test environment info
Environment: .venv
Absolute path: D:\projects\v-JianzhangDong_25_12_08_case1\vsc-5mini-mix22-arm5-s270\v-JianzhangDong_25_12_08_case1\.venv
Python 3.14.0 -- pip 25.3 from D:\projects\v-JianzhangDong_25_12_08_case1\vsc-5mini-mix22-arm5-s270\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)


## Last auto_test environment info
Environment: .venv
Absolute path: D:\projects\v-JianzhangDong_25_12_08_case1\vsc-5mini-mix22-arm5-s270\v-JianzhangDong_25_12_08_case1\.venv
Python 3.14.0 -- pip 25.3 from D:\projects\v-JianzhangDong_25_12_08_case1\vsc-5mini-mix22-arm5-s270\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)


## Last auto_test environment info
Environment: .venv
Absolute path: D:\projects\v-JianzhangDong_25_12_08_case1\vsc-5mini-mix22-arm5-s270\v-JianzhangDong_25_12_08_case1\.venv
Python 3.14.0 -- pip 25.3 from D:\projects\v-JianzhangDong_25_12_08_case1\vsc-5mini-mix22-arm5-s270\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)
