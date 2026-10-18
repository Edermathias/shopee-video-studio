#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
[ -d .venv ] || python3 -m venv .venv
source .venv/bin/activate
pip install -q -r requirements.txt
python check_env.py
echo "Abrindo em http://localhost:8000"
uvicorn app.main:app --port 8000
