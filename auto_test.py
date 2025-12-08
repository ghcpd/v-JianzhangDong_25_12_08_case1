#!/usr/bin/env python3
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV_DIR = ROOT / '.venv'
LOGS_DIR = ROOT / 'logs'
LOGS_DIR.mkdir(exist_ok=True)
LOG_FILE = LOGS_DIR / 'test_run.log'

def run(cmd, env=None, capture=False):
    print('Running:', ' '.join(cmd))
    proc = subprocess.run(cmd, env=env, stdout=subprocess.PIPE if capture else None, stderr=subprocess.STDOUT)
    return proc

# Recreate venv only if we are not already running inside it
already_active = (sys.executable.startswith(str(VENV_DIR)))
if VENV_DIR.exists() and not already_active:
    print('Removing existing .venv')
    import shutil
    shutil.rmtree(VENV_DIR)

if not VENV_DIR.exists():
    print('Creating virtual environment...')
    subprocess.check_call([sys.executable, '-m', 'venv', str(VENV_DIR)])

# Paths
if os.name == 'nt':
    python_bin = VENV_DIR / 'Scripts' / 'python.exe'
    pip_bin = VENV_DIR / 'Scripts' / 'pip.exe'
else:
    python_bin = VENV_DIR / 'bin' / 'python'
    pip_bin = VENV_DIR / 'bin' / 'pip'

# Upgrade pip and install requirements only if not already active venv
if not already_active:
    subprocess.check_call([str(pip_bin), 'install', '--upgrade', 'pip', 'setuptools', 'wheel'])
    subprocess.check_call([str(pip_bin), 'install', '-r', str(ROOT / 'requirements.txt')])

# Run each test script in the tests/ directory and write logs
with open(LOG_FILE, 'w', encoding='utf-8') as fh:
    fh.write('Test run log\n')
    fh.write('================\n')
    for test_file in sorted((ROOT / 'tests').glob('*.py')):
        fh.write(f'Running {test_file.name}\n')
        env = os.environ.copy()
        env['PYTHONPATH'] = str(ROOT)
        proc = subprocess.run([str(python_bin), str(test_file)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env)
        fh.write(proc.stdout.decode('utf-8', errors='replace'))
        fh.write('\n')

# Append environment info to README.md
readme = ROOT / 'README.md'
py_ver = subprocess.check_output([str(python_bin), '--version']).decode().strip()
pip_ver = subprocess.check_output([str(python_bin), '-m', 'pip', '--version']).decode().strip()
info = f"\nEnvironment: .venv\nPath: {VENV_DIR}\nPython: {py_ver}\nPip: {pip_ver}\n"
if readme.exists():
    existing = readme.read_text(encoding='utf-8')
    readme.write_text(existing + info, encoding='utf-8')
else:
    readme.write_text(info, encoding='utf-8')

print('Done. Logs written to', LOG_FILE)
