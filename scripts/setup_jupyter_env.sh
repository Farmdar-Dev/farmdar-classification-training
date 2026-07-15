#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if command -v python >/dev/null 2>&1; then
  PYTHON=python
elif command -v python3 >/dev/null 2>&1; then
  PYTHON=python3
else
  echo "Python was not found. Install Python 3.11 or newer first."
  exit 1
fi

"$PYTHON" -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name farmdar-classification-training --display-name "Python (Farmdar Classification Training)"

echo
echo "Setup complete."
echo "In VS Code, open this folder and select this notebook kernel:"
echo "Python (Farmdar Classification Training)"
