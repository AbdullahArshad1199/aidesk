from fastapi import APIRouter, Query
from typing import List, Dict, Any
from utils.fetch_youtube import fetch_all_youtube_videos
from utils.cache import cache

router = APIRouter()

@router.get("")
async def get_videos(category: str = Query(None, description="Filter by category: talks, demos, research")):
    """Get AI-related videos."""
    cached = cache.get("all_videos")
    if cached and not category:
        return cached
    
    videos = await fetch_all_youtube_videos()
    
    # Filter by category if provided
    if category:
        category_lower = category.lower()
        filtered = []
        for video in videos:
            title_lower = video.get("title", "").lower()
            desc_lower = video.get("description", "").lower()
            
            if category_lower == "talks" and ("talk" in title_lower or "conference" in title_lower or "presentation" in title_lower):
                filtered.append(video)
            elif category_lower == "demos" and ("demo" in title_lower or "demonstration" in title_lower or "showcase" in title_lower):
                filtered.append(video)
            elif category_lower == "research" and ("research" in title_lower or "paper" in title_lower or "study" in title_lower):
                filtered.append(video)
        
        videos = filtered
    
    result = {"videos": videos, "count": len(videos)}
    
    if not category:
        cache.set("all_videos", result)
    
    return result

