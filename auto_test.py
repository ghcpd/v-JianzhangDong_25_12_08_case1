#!/usr/bin/env python3
"""
auto_test.py

Detects and uses the .venv/python interpreter to run all tests under the tests/ folder.
Writes output to logs/test_run.log and appends environment details to README.md.
"""
import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV_DIR = ROOT / '.venv'

def find_python_in_venv(venv_dir: Path) -> str:
    if sys.platform.startswith('win'):
        candidate = venv_dir / 'Scripts' / 'python.exe'
    else:
        candidate = venv_dir / 'bin' / 'python'
    if candidate.exists():
        return str(candidate)
    raise FileNotFoundError(f"No python executable found in {venv_dir}")

def run_tests(python_exe: str, tests_dir: Path, log_path: Path) -> int:
    """
    Execute every .py file under tests/ using the venv python. Writes combined output to the log.
    Returns 0 if all scripts exit 0; otherwise return the first non-zero exit code.
    """
    log_path.parent.mkdir(parents=True, exist_ok=True)
    exit_code = 0
    test_files = sorted([p for p in tests_dir.glob('*.py') if p.is_file()])
    with open(log_path, 'w', encoding='utf-8') as fh:
        if not test_files:
            fh.write('No test scripts found in tests/\n')
        for t in test_files:
            fh.write(f'=== Running {t.name} ===\n')
            # Ensure project root is available on PYTHONPATH so tests can import the `app` package
            env = os.environ.copy()
            env['PYTHONPATH'] = str(ROOT)
            proc = subprocess.run([python_exe, str(t)], stdout=fh, stderr=subprocess.STDOUT, text=True, env=env, cwd=str(ROOT))
            fh.write(f'=== Exit {proc.returncode} for {t.name} ===\n\n')
            if proc.returncode != 0 and exit_code == 0:
                exit_code = proc.returncode
    return exit_code

def capture_env_info(python_exe: str) -> dict:
    # Query python and pip versions inside the venv
    info = {}
    try:
        out = subprocess.check_output([python_exe, '-c', 'import sys; print(sys.version.replace("\\n"," "))'], text=True)
        info['python'] = out.strip()
    except Exception:
        info['python'] = 'unknown'
    try:
        out = subprocess.check_output([python_exe, '-m', 'pip', '--version'], text=True)
        info['pip'] = out.strip()
    except Exception:
        info['pip'] = 'unknown'
    return info

def append_readme(info: dict, readme_path: Path, venv_dir: Path):
    into = []
    into.append('\n---')
    into.append('\nEnvironment report (auto_test):')
    into.append(f"\n- venv: {venv_dir.name}")
    into.append(f"\n- absolute_path: {str(venv_dir.resolve())}")
    into.append(f"\n- python: {info.get('python','unknown')}")
    into.append(f"\n- pip: {info.get('pip','unknown')}")
    readme_path.parent.mkdir(parents=True, exist_ok=True)
    with open(readme_path, 'a', encoding='utf-8') as fh:
        fh.writelines(into)

def main():
    tests_dir = ROOT / 'tests'
    log_path = ROOT / 'logs' / 'test_run.log'
    readme_path = ROOT / 'README.md'

    if not VENV_DIR.exists():
        print('.venv not found in the repository root. Please run setup.sh or create the environment first.')
        sys.exit(2)

    python_exe = find_python_in_venv(VENV_DIR)
    print(f'Using python from {python_exe}')

    print('Running tests...')
    rc = run_tests(python_exe, tests_dir, log_path)
    print(f'Test run finished with exit code {rc}. Logs written to {log_path}')

    env_info = capture_env_info(python_exe)
    append_readme(env_info, readme_path, VENV_DIR)

    sys.exit(rc)

if __name__ == '__main__':
    main()
