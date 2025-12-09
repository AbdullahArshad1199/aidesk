from fastapi import APIRouter, Query
from typing import List, Dict, Any
from routers import news
from utils.fetch_youtube import fetch_all_youtube_videos
from utils.cache import cache

router = APIRouter()

@router.get("")
async def search(q: str = Query(..., description="Search query")):
    """Search across news and videos."""
    query_lower = q.lower()
    
    # Check cache
    cache_key = f"search_{q}"
    cached = cache.get(cache_key)
    if cached:
        return cached
    
    # Get all news
    all_news = await news.get_all_news()
    
    # Search in news
    news_results = []
    for article in all_news:
        title = article.get("title", "").lower()
        description = article.get("description", "").lower()
        source = article.get("source", "").lower()
        
        if query_lower in title or query_lower in description or query_lower in source:
            news_results.append(article)
    
    # Get all videos
    all_videos_data = await fetch_all_youtube_videos()
    all_videos = all_videos_data if isinstance(all_videos_data, list) else []
    
    # Search in videos
    video_results = []
    for video in all_videos:
        title = video.get("title", "").lower()
        description = video.get("description", "").lower()
        channel = video.get("channel", "").lower()
        
        if query_lower in title or query_lower in description or query_lower in channel:
            video_results.append(video)
    
    result = {
        "query": q,
        "news": news_results,
        "videos": video_results,
        "news_count": len(news_results),
        "videos_count": len(video_results)
    }
    
    cache.set(cache_key, result)
    return result

