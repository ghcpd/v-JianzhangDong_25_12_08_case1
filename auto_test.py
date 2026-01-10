import os
import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
VENV = ROOT / '.venv'
LOGS = ROOT / 'logs'
LOGS.mkdir(exist_ok=True)

if VENV.exists():
    # pick python from venv
    if sys.platform == 'win32':
        py = VENV / 'Scripts' / 'python.exe'
    else:
        py = VENV / 'bin' / 'python'
else:
    py = Path(sys.executable)

print(f"Using Python interpreter: {py}")

results = []
for test_file in sorted((ROOT / 'tests').glob('case_*.py')):
    log_path = LOGS / (test_file.stem + '.log')
    cmd = [str(py), str(test_file)]
    print(f"Running: {' '.join(cmd)}")
    env = os.environ.copy()
    # Ensure the project root is on PYTHONPATH so tests can import local app/ package
    env['PYTHONPATH'] = str(ROOT) + os.pathsep + env.get('PYTHONPATH', '')
    proc = subprocess.run(cmd, capture_output=True, text=True, env=env)
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write(proc.stdout)
        f.write('\n')
        f.write(proc.stderr)
    results.append((test_file.name, proc.returncode))

# Append environment info to README.md
import platform
py_ver = subprocess.check_output([str(py), '-V']).decode().strip()
try:
    pip_ver = subprocess.check_output([str(py), '-m', 'pip', '--version']).decode().strip()
except Exception:
    pip_ver = 'pip not available'

readme = ROOT / 'README.md'
with open(readme, 'a', encoding='utf-8') as f:
    f.write('\n')
    f.write('Environment: .venv\n')
    f.write(f'Absolute path: {VENV}\n')
    f.write(f'Python/pip: {py_ver} / {pip_ver}\n')

# Produce summary
summary = LOGS / 'test_run.log'
with open(summary, 'w', encoding='utf-8') as f:
    for name, code in results:
        f.write(f"{name}: {'PASS' if code == 0 else 'FAIL'} (exit {code})\n")

print('Test run complete. Summary:')
with open(summary) as f:
    print(f.read())
