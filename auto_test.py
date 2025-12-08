#!/usr/bin/env python3
import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV = ROOT / '.venv'
LOGS = ROOT / 'logs'
LOGS.mkdir(exist_ok=True)
LOGFILE = LOGS / 'test_run.log'

# Determine venv python
if os.name == 'nt':
    venv_python = VENV / 'Scripts' / 'python.exe'
else:
    venv_python = VENV / 'bin' / 'python'

if not venv_python.exists():
    print('.venv not found or missing python interpreter. Run setup.sh first to create it.')
    sys.exit(1)

with open(LOGFILE, 'a', encoding='utf-8') as out:
    out.write(f'Test run started: {subprocess.getoutput("date /T && time /T" ) if os.name=="nt" else subprocess.getoutput("date") }\n')

    tests_dir = ROOT / 'tests'
    env = os.environ.copy()
    env['PYTHONPATH'] = str(ROOT)
    for test in sorted(tests_dir.glob('*.py')):
        out.write(f'---- Running {test.name} ----\n')
        proc = subprocess.run([str(venv_python), str(test)], capture_output=True, text=True, env=env)
        out.write(proc.stdout)
        out.write(proc.stderr)
        out.write(f'Exit code: {proc.returncode}\n')

# Append environment and python/pip versions to README.md
try:
    py_ver = subprocess.check_output([str(venv_python), '--version'], text=True).strip()
    pip_ver = subprocess.check_output([str(venv_python), '-m', 'pip', '--version'], text=True).strip()
except subprocess.CalledProcessError:
    py_ver = 'unknown'
    pip_ver = 'unknown'

readme = ROOT / 'README.md'
with open(readme, 'a', encoding='utf-8') as r:
    r.write('\n\n## Last auto_test environment info\n')
    r.write(f'Environment: .venv\n')
    r.write(f'Absolute path: {VENV.resolve()}\n')
    r.write(f'{py_ver} -- {pip_ver}\n')

print('Test run complete. See logs/test_run.log for details.')
