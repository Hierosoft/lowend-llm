if (-not (Test-Path ".venv" -PathType Container)) {
    Write-Error "Error: You must first setup .venv according to the readme."
    exit 1
}

& .\.venv\Scripts\python.exe local-chat.py @Args
