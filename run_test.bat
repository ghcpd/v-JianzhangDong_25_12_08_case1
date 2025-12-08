@echo off
if exist .venv\Scripts\activate (
  call .venv\Scripts\activate
  set PY=.venv\Scripts\python.exe
) else (
  set PY=python
)
if not exist logs mkdir logs
%PY% -u tests\case_1.py > logs\case_1.log
%PY% -u tests\case_2.py > logs\case_2.log
%PY% -u tests\case_3.py > logs\case_3.log
echo All tests executed. Logs saved to logs\
