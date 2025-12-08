# Project environment & test helpers

This repository includes auto-generated helpers to reproduce a clean environment and run tests across platforms.

## Generated files (overview)
- `requirements_backup.txt` - backup of the original requirements file (untouched)
- `requirements.txt` - updated, pinned dependency versions (secure and compatible)
- `report.json` - simple report listing updated packages and reasons
- `Dockerfile` - container recipe using Python 3.14 and a venv under `/opt/venv`
- `setup.sh` - script to create a fresh `.venv` and install deps (macOS/Linux)
- `run_test.sh` - run tests inside `.venv` and write logs (macOS/Linux)
- `run_test.bat` - same as above for Windows
- `auto_test.py` - programmatic test runner that uses `.venv`, writes `logs/test_run.log` and appends environment info to README.md
- `.gitignore` - updated to exclude `.venv/` and `logs/`

## Setup (Linux/macOS)
1. Ensure Python 3.14 is installed and available as `python3` or `python`.
2. Create a fresh virtual environment and install requirements:

```bash
./setup.sh
```

## Setup (Windows / PowerShell)
1. Ensure Python 3.14 is installed and available as `python`.
2. Create a fresh virtual environment and install requirements (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\python -m pip install --upgrade pip setuptools wheel; .\.venv\Scripts\pip install -r requirements.txt
```

## Run tests
- Linux/macOS: `./run_test.sh` (writes logs/test_run.log)
- Windows (cmd): `run_test.bat` (writes logs\test_run.log)

## auto_test.py
This script automatically detects `.venv/`, runs all tests in `tests/` using the `.venv` interpreter, writes the combined output to `logs/test_run.log`, and appends the environment name, absolute path and Python/pip versions to this `README.md`.

Example usage:

```bash
python auto_test.py
```

## Logs
All runtime output from the automated test runs is stored in `logs/test_run.log`. Use this file to inspect failures and debugging output.

---
Environment report (auto_test):
- venv: .venv
- absolute_path: D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv
- python: unknown
- pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)
---
Environment report (auto_test):
- venv: .venv
- absolute_path: D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv
- python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
- pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)
---
Environment report (auto_test):
- venv: .venv
- absolute_path: D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv
- python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
- pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)
---
Environment report (auto_test):
- venv: .venv
- absolute_path: D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv
- python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
- pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)
---
Environment report (auto_test):
- venv: .venv
- absolute_path: D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv
- python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
- pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)
---
Environment report (auto_test):
- venv: .venv
- absolute_path: D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv
- python: 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)]
- pip: pip 25.3 from D:\vscoderprojects\v-JianzhangDong_25_12_08_case1\oswe-mini-secondary\v-JianzhangDong_25_12_08_case1\.venv\Lib\site-packages\pip (python 3.14)