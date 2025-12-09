import os
import httpx
from typing import List, Dict, Any
from datetime import datetime
from utils.clean_data import parse_date

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "")

YOUTUBE_CHANNELS = [
    {"id": "UCr0ail1RdXdusqeqco44loA", "name": "OpenAI"},
    {"id": "UC0e3QhIYukixgh5VVpKHH9Q", "name": "Google Research"},
    {"id": "UC0e3QhIYukixgh5VVpKHH9Q", "name": "DeepMind"},
    {"id": "UCqk7Cd8Lv1sqG3Jpq3BnsGw", "name": "Anthropic"},
]

YOUTUBE_SEARCH_QUERIES = [
    "artificial intelligence research",
    "AI breakthrough",
    "machine learning conference",
    "ICLR",
    "NeurIPS",
    "AI safety",
    "AGI research"
]

async def fetch_youtube_videos(channel_id: str = None, query: str = None, max_results: int = 10) -> List[Dict[str, Any]]:
    """Fetch videos from YouTube API."""
    if not YOUTUBE_API_KEY:
        # Return mock data if no API key
        return get_mock_videos()
    
    try:
        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "type": "video",
            "maxResults": max_results,
            "order": "date",
            "key": YOUTUBE_API_KEY
        }
        
        if channel_id:
            params["channelId"] = channel_id
        if query:
            params["q"] = query
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            videos = []
            for item in data.get("items", []):
                snippet = item.get("snippet", {})
                video = {
                    "id": item.get("id", {}).get("videoId", ""),
                    "title": snippet.get("title", ""),
                    "description": snippet.get("description", ""),
                    "thumbnail": snippet.get("thumbnails", {}).get("high", {}).get("url", ""),
                    "channel": snippet.get("channelTitle", ""),
                    "published_at": snippet.get("publishedAt", ""),
                    "channel_id": snippet.get("channelId", "")
                }
                
                if video["published_at"]:
                    video["published_at"] = parse_date(video["published_at"]).isoformat()
                else:
                    video["published_at"] = datetime.now().isoformat()
                
                if video["id"] and video["title"]:
                    videos.append(video)
            
            return videos
    except Exception as e:
        print(f"Error fetching YouTube: {e}")
        return get_mock_videos()

async def fetch_all_youtube_videos() -> List[Dict[str, Any]]:
    """Fetch videos from multiple sources."""
    import asyncio
    
    tasks = []
    
    # Fetch from channels
    for channel in YOUTUBE_CHANNELS[:3]:  # Limit to avoid rate limits
        tasks.append(fetch_youtube_videos(channel_id=channel["id"], max_results=5))
    
    # Fetch from search queries
    for query in YOUTUBE_SEARCH_QUERIES[:3]:
        tasks.append(fetch_youtube_videos(query=query, max_results=5))
    
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    all_videos = []
    seen_ids = set()
    
    for result in results:
        if isinstance(result, list):
            for video in result:
                if video["id"] not in seen_ids:
                    seen_ids.add(video["id"])
                    all_videos.append(video)
        elif isinstance(result, Exception):
            print(f"Error in YouTube fetch: {result}")
    
    # Sort by date
    all_videos.sort(key=lambda x: x.get("published_at", ""), reverse=True)
    
    return all_videos[:50]  # Limit to 50 videos

def get_mock_videos() -> List[Dict[str, Any]]:
    """Return mock video data when API key is not available."""
    return [
        {
            "id": "dQw4w9WgXcQ",
            "title": "AI Research Breakthrough: Understanding Large Language Models",
            "description": "Exploring the latest advances in AI research and LLM capabilities.",
            "thumbnail": "https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg",
            "channel": "OpenAI",
            "published_at": datetime.now().isoformat(),
            "channel_id": "UCr0ail1RdXdusqeqco44loA"
        },
        {
            "id": "jNQXAC9IVRw",
            "title": "DeepMind: Latest AI Safety Research",
            "description": "DeepMind researchers discuss AI safety and alignment.",
            "thumbnail": "https://img.youtube.com/vi/jNQXAC9IVRw/maxresdefault.jpg",
            "channel": "DeepMind",
            "published_at": datetime.now().isoformat(),
            "channel_id": "UC0e3QhIYukixgh5VVpKHH9Q"
        }
    ]

