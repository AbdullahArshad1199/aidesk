# AI News Hub - Backend

FastAPI backend for aggregating AI news and videos.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. (Optional) Set API keys in `.env`:
```
NEWSAPI_KEY=your_key
BING_API_KEY=your_key
YOUTUBE_API_KEY=your_key
```

3. Run the server:
```bash
uvicorn main:app --reload --port 8000
```

## Endpoints

- `GET /news/all` - Get all news articles
- `GET /news/trending` - Get trending news
- `GET /news/important` - Get important news
- `GET /videos` - Get AI videos
- `GET /videos?category=talks` - Filter videos by category
- `GET /search?q=query` - Search news and videos

