@echo off
cd /d %~dp0

call .venv\Scripts\activate
pip install -e . >nul 2>&1

py -m monprojet
pause