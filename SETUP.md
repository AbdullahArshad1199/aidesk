# Setup and Run Commands

## 🚀 Quick Start Commands

### Prerequisites
- Python 3.8+ installed
- Node.js 18+ installed
- npm or yarn installed

---

## 📦 Backend Setup (FastAPI)

### Step 1: Navigate to backend directory
```bash
cd backend
```

### Step 2: Install Python dependencies
```bash
pip install -r requirements.txt
```

### Step 3: (Optional) Set API keys
Create a `.env` file in the `backend` directory:
```bash
# Windows PowerShell
New-Item -Path .env -ItemType File

# Then add these lines (optional):
NEWSAPI_KEY=your_newsapi_key_here
BING_API_KEY=your_bing_api_key_here
YOUTUBE_API_KEY=your_youtube_api_key_here
```

### Step 4: Start the backend server
```bash
# Option 1: Using Python module (Recommended)
python -m uvicorn main:app --reload --port 8000

# Option 2: Using startup script (Windows)
.\start.ps1
# or
.\start.bat
```

**Backend will run on:** `http://localhost:8000`

**API Documentation:** `http://localhost:8000/docs`

---

## 🎨 Frontend Setup (Next.js)

### Step 1: Navigate to project root
```bash
# If you're in backend directory, go back
cd ..
```

### Step 2: Install dependencies
```bash
npm install
```

### Step 3: (Optional) Set environment variable
Create `.env.local` file in the root directory:
```bash
# Windows PowerShell
New-Item -Path .env.local -ItemType File

# Then add:
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### Step 4: Start the frontend development server
```bash
npm run dev
```

**Frontend will run on:** `http://localhost:3000`

---

## 🎯 Complete Setup (Both Backend & Frontend)

### Terminal 1 - Backend:
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

### Terminal 2 - Frontend:
```bash
npm install
npm run dev
```

---

## 📝 Available Commands

### Backend Commands
```bash
# Start server
python -m uvicorn main:app --reload --port 8000

# Start server (production mode)
python -m uvicorn main:app --host 0.0.0.0 --port 8000

# Check if server is running
curl http://localhost:8000/health
```

### Frontend Commands
```bash
# Development server
npm run dev

# Build for production
npm run build

# Start production server
npm start

# Run linter
npm run lint
```

---

## 🔍 Verify Installation

### Check Backend:
1. Open browser: `http://localhost:8000/docs`
2. You should see FastAPI Swagger documentation
3. Test endpoint: `http://localhost:8000/health`

### Check Frontend:
1. Open browser: `http://localhost:3000`
2. You should see the AI News Hub homepage

---

## 🐛 Troubleshooting

### Backend Issues:
```bash
# If uvicorn not found:
pip install uvicorn[standard]

# If dependencies missing:
pip install -r requirements.txt --upgrade

# Check Python version:
python --version  # Should be 3.8+
```

### Frontend Issues:
```bash
# Clear cache and reinstall:
rm -rf node_modules package-lock.json
npm install

# Check Node version:
node --version  # Should be 18+
```

### Port Already in Use:
```bash
# Backend (change port):
python -m uvicorn main:app --reload --port 8001

# Frontend (change port):
npm run dev -- -p 3001
```

---

## 📚 Project Structure
```
marks/
├── backend/          # FastAPI backend
│   ├── main.py      # Start here
│   └── requirements.txt
├── app/              # Next.js frontend
│   └── page.tsx     # Home page
└── package.json     # Frontend dependencies
```

---

## ✅ Success Checklist

- [ ] Backend dependencies installed
- [ ] Backend server running on port 8000
- [ ] Frontend dependencies installed
- [ ] Frontend server running on port 3000
- [ ] Can access `http://localhost:3000`
- [ ] Can access `http://localhost:8000/docs`

