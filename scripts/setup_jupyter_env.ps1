$ErrorActionPreference = "Stop"

Set-Location (Join-Path $PSScriptRoot "..")

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    $python = Get-Command py -ErrorAction SilentlyContinue
}
if (-not $python) {
    throw "Python was not found. Install Python 3.11 or newer first."
}

if ($python.Name -eq "py.exe" -or $python.Name -eq "py") {
    py -3 -m venv .venv
} else {
    python -m venv .venv
}

.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m ipykernel install --user --name farmdar-classification-training --display-name "Python (Farmdar Classification Training)"

Write-Host ""
Write-Host "Setup complete."
Write-Host "In VS Code, open this folder and select this notebook kernel:"
Write-Host "Python (Farmdar Classification Training)"
