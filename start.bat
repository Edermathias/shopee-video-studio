@echo off
cd /d "%~dp0"
if not exist .venv python -m venv .venv
call .venv\Scripts\activate
pip install -q -r requirements.txt
python check_env.py
echo Abrindo em http://localhost:8000
uvicorn app.main:app --port 8000
