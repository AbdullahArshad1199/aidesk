# Start script for AI News Hub
# This script starts both backend and frontend servers

Write-Host "🚀 Starting AI News Hub..." -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
$pythonCmd = Get-Command python -ErrorAction SilentlyContinue
if (-not $pythonCmd) {
    Write-Host "❌ Python is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Python 3.8+ and try again" -ForegroundColor Yellow
    exit 1
}

# Check if Node.js is installed
$nodeCmd = Get-Command node -ErrorAction SilentlyContinue
if (-not $nodeCmd) {
    Write-Host "❌ Node.js is not installed or not in PATH" -ForegroundColor Red
    Write-Host "Please install Node.js 18+ and try again" -ForegroundColor Yellow
    exit 1
}

Write-Host "✅ Python and Node.js are installed" -ForegroundColor Green
Write-Host ""

# Start Backend
Write-Host "📦 Starting Backend Server..." -ForegroundColor Yellow
$backendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    Set-Location backend
    python -m uvicorn main:app --reload --port 8000
}

# Wait a bit for backend to start
Start-Sleep -Seconds 3

# Start Frontend
Write-Host "🎨 Starting Frontend Server..." -ForegroundColor Yellow
$frontendJob = Start-Job -ScriptBlock {
    Set-Location $using:PWD
    npm run dev
}

Write-Host ""
Write-Host "✅ Both servers are starting..." -ForegroundColor Green
Write-Host ""
Write-Host "📍 Backend API: http://localhost:8000" -ForegroundColor Cyan
Write-Host "📍 Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host "📍 API Docs: http://localhost:8000/docs" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C to stop both servers" -ForegroundColor Yellow
Write-Host ""

# Wait for jobs
try {
    Wait-Job -Job $backendJob, $frontendJob
} catch {
    Write-Host "Stopping servers..." -ForegroundColor Yellow
    Stop-Job -Job $backendJob, $frontendJob
    Remove-Job -Job $backendJob, $frontendJob
}

