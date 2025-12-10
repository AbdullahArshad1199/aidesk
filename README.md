# AI News Hub

A complete full-stack application for aggregating and displaying AI-related news and videos from multiple sources.

## 🚀 Features

- **News Aggregation**: Fetches AI news from RSS feeds (Google News, TechCrunch, OpenAI, DeepMind, Anthropic)
- **Smart Categorization**: Automatically categorizes news as Trending or Important
- **Video Collection**: Aggregates AI videos from YouTube
- **Search Functionality**: Search across all news and videos
- **Modern UI**: Beautiful navy-blue themed interface with responsive design
- **Real-time Updates**: In-memory caching with 10-15 minute TTL

## 📁 Project Structure

```
.
├── backend/           # FastAPI backend
│   ├── main.py       # FastAPI app
│   ├── routers/      # API routes
│   └── utils/        # Utilities (RSS, YouTube, cache)
├── app/              # Next.js frontend
│   ├── components/   # React components
│   ├── videos/       # Videos page
│   ├── search/       # Search page
│   └── news/         # News detail pages
└── package.json      # Frontend dependencies
```

## 🛠️ Setup

### Quick Start

**Terminal 1 - Backend:**
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload --port 8000
```

**Terminal 2 - Frontend:**
```bash
npm install
npm run dev
```

Then open [http://localhost:3000](http://localhost:3000) in your browser.

### Detailed Setup

#### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Set API keys in `.env`:
```
NEWSAPI_KEY=your_key
BING_API_KEY=your_key
YOUTUBE_API_KEY=your_key
```

4. Run the FastAPI server:
```bash
python -m uvicorn main:app --reload --port 8000
```

**Backend runs on:** `http://localhost:8000`  
**API Docs:** `http://localhost:8000/docs`

#### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Set environment variable (optional):
```bash
# Create .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Run the development server:
```bash
npm run dev
```

5. Open [http://localhost:3000](http://localhost:3000) in your browser

For more detailed setup instructions, see [SETUP.md](./SETUP.md)

## 📡 API Endpoints

- `GET /news/all` - Get all news articles
- `GET /news/trending` - Get trending news
- `GET /news/important` - Get important news
- `GET /videos` - Get all videos
- `GET /videos?category=talks` - Filter videos by category
- `GET /search?q=query` - Search news and videos

## 🎨 Design

The application uses a navy-blue color scheme:
- Primary: `#0A1A3A`
- Secondary: `#112B54`
- Accent: `#4A6FF3`
- Background: `#EEF2FF`

## 📝 Notes

- The backend works without API keys (uses RSS feeds by default)
- YouTube API key is optional (falls back to mock data)
- All data is cached in memory for 10-15 minutes
- No database required - fully real-time

## 🚀 Deployment

### Backend
Deploy to services like:
- Railway
- Render
- Heroku
- DigitalOcean

### Frontend
Deploy to:
- Vercel (recommended)
- Netlify
- Any static hosting service

Make sure to set `NEXT_PUBLIC_API_URL` to your backend URL in production.

