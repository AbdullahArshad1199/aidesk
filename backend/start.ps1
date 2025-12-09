Write-Host "Starting AI News Hub Backend..." -ForegroundColor Green
python -m uvicorn main:app --reload --port 8000

