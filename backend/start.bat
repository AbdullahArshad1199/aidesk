@echo off
echo Starting AI News Hub Backend...
python -m uvicorn main:app --reload --port 8000
pause

