@echo off
echo Starting AI News Hub...
echo.

REM Start Backend in a new window
start "AI News Hub - Backend" cmd /k "cd backend && python -m uvicorn main:app --reload --port 8000"

REM Wait a bit for backend to start
timeout /t 3 /nobreak >nul

REM Start Frontend in a new window
start "AI News Hub - Frontend" cmd /k "npm run dev"

echo.
echo Both servers are starting in separate windows...
echo.
echo Backend API: http://localhost:8000
echo Frontend: http://localhost:3000
echo API Docs: http://localhost:8000/docs
echo.
echo Close the windows to stop the servers.
pause

