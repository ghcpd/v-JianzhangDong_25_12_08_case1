import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV = ROOT / '.venv'
LOGS = ROOT / 'logs'
LOGS.mkdir(exist_ok=True)
LOG_FILE = LOGS / 'test_run.log'

def python_exe():
    if (VENV / 'Scripts' / 'python.exe').exists():
        return str(VENV / 'Scripts' / 'python.exe')
    return sys.executable

def pip_exe():
    if (VENV / 'Scripts' / 'python.exe').exists():
        return str(VENV / 'Scripts' / 'python.exe') + ' -m pip'
    return sys.executable + ' -m pip'

def run_tests():
    py = python_exe()
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write('=== Test run start ===\n')
        f.write(f'Python: {subprocess.check_output([py, "--version"]).decode().strip()}\n')
        try:
            # Prefer pytest if importable; otherwise run test scripts directly
            can_use_pytest = False
            try:
                imp = subprocess.run([py, '-c', 'import pytest; print(pytest.__version__)'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if imp.returncode == 0:
                    can_use_pytest = True
            except Exception:
                can_use_pytest = False

            if can_use_pytest:
                proc = subprocess.run([py, '-m', 'pytest', '-q', 'tests'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                out = proc.stdout or ''
                f.write(out)
                # If pytest reports no tests ran, fallback to direct script execution
                if 'no tests ran' in out.lower() or 'collected 0' in out.lower():
                    f.write('\npytest did not collect tests; falling back to direct execution of test scripts.\n')
                    for t in sorted((Path('tests')).glob('case_*.py')):
                        f.write(f'--- Running {t} ---\n')
                        try:
                            proc2 = subprocess.run([py, str(t)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
                            f.write(proc2.stdout + '\n')
                        except Exception as e:
                            f.write(f'Error running {t}: {e}\n')
            else:
                # Fallback: run each test script directly and capture stdout/stderr
                for t in sorted((Path('tests')).glob('case_*.py')):
                    f.write(f'--- Running {t} ---\n')
                    try:
                        # Run the test script with PYTHONPATH set so `app` can be imported
                        env = os.environ.copy()
                        env['PYTHONPATH'] = str(ROOT)
                        f.write(f"PYTHONPATH passed to subprocess: {env.get('PYTHONPATH')}\n")
                        proc2 = subprocess.run([py, str(t)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, env=env)
                        f.write(proc2.stdout + '\n')
                    except Exception as e:
                        f.write(f'Error running {t}: {e}\n')
            f.write('\n=== Test run end ===\n')
        except Exception as e:
            f.write(f'Error running tests: {e}\n')

def append_env_info():
    py = python_exe()
    pip = pip_exe()
    info = []
    env_name = VENV.name if VENV.exists() else '.venv'
    info.append(f'Environment: {env_name}')
    info.append(f'Path: {str(VENV)}')
    try:
        pyv = subprocess.check_output([py, '--version']).decode().strip()
    except Exception:
        pyv = 'unknown'
    try:
        pipv = subprocess.check_output(pip.split() + ['--version']).decode().strip()
    except Exception:
        pipv = 'unknown'
    info.append(f'Python: {pyv}')
    info.append(f'Pip: {pipv}')
    readme = ROOT / 'README.md'
    with open(readme, 'a', encoding='utf-8') as f:
        f.write('\n\n-- Environment Info --\n')
        for line in info:
            f.write(line + '\n')

if __name__ == '__main__':
    run_tests()
    append_env_info()
