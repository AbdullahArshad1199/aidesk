from fastapi import APIRouter, Query
from typing import List, Dict, Any
from datetime import datetime
from utils.fetch_rss import fetch_all_rss_feeds
from utils.fetch_newsapi import fetch_all_news_apis
from utils.clean_data import deduplicate_articles, categorize_article, parse_date
from utils.fetch_article_content import fetch_article_content
from utils.cache import cache

router = APIRouter()

async def get_all_news() -> List[Dict[str, Any]]:
    """Internal function to fetch all news."""
    # Check cache
    cached = cache.get("all_news")
    if cached:
        return cached
    
    # Fetch from all sources
    rss_articles = await fetch_all_rss_feeds()
    api_articles = await fetch_all_news_apis()
    
    all_articles = rss_articles + api_articles
    
    # Deduplicate
    all_articles = deduplicate_articles(all_articles)
    
    # Sort by date (with error handling)
    try:
        all_articles.sort(key=lambda x: parse_date(x.get("published_at", "")), reverse=True)
    except Exception as e:
        print(f"Error sorting articles: {e}")
        # Sort by title as fallback
        all_articles.sort(key=lambda x: x.get("title", ""), reverse=True)
    
    # Categorize each article
    for article in all_articles:
        categories = categorize_article(article, all_articles)
        article["is_trending"] = categories["trending"]
        article["is_important"] = categories["important"]
    
    # Cache results
    cache.set("all_news", all_articles)
    
    return all_articles

@router.get("/all")
async def get_news_all():
    """Get all news articles."""
    try:
        articles = await get_all_news()
        return {"articles": articles, "count": len(articles)}
    except Exception as e:
        print(f"Error in get_news_all: {e}")
        import traceback
        traceback.print_exc()
        return {"articles": [], "count": 0, "error": str(e)}

@router.get("/trending")
async def get_news_trending():
    """Get trending news articles."""
    try:
        cached = cache.get("trending_news")
        if cached:
            return cached
        
        all_articles = await get_all_news()
        trending = [a for a in all_articles if a.get("is_trending", False)]
        
        # If no trending articles found, use the most recent 10 articles as trending
        if len(trending) == 0 and len(all_articles) > 0:
            trending = all_articles[:10]
            # Mark them as trending
            for article in trending:
                article["is_trending"] = True
        
        result = {"articles": trending, "count": len(trending)}
        cache.set("trending_news", result)
        return result
    except Exception as e:
        print(f"Error in get_news_trending: {e}")
        import traceback
        traceback.print_exc()
        return {"articles": [], "count": 0, "error": str(e)}

@router.get("/important")
async def get_news_important():
    """Get important news articles."""
    try:
        cached = cache.get("important_news")
        if cached:
            return cached
        
        all_articles = await get_all_news()
        important = [a for a in all_articles if a.get("is_important", False)]
        
        result = {"articles": important, "count": len(important)}
        cache.set("important_news", result)
        return result
    except Exception as e:
        print(f"Error in get_news_important: {e}")
        import traceback
        traceback.print_exc()
        return {"articles": [], "count": 0, "error": str(e)}

@router.get("/content")
async def get_article_content(url: str = Query(..., description="Article URL")):
    """Get full article content from source."""
    try:
        # Check cache
        cache_key = f"article_content_{url}"
        cached = cache.get(cache_key)
        if cached:
            return cached
        
        # Fetch content
        content_data = await fetch_article_content(url)
        
        if content_data:
            cache.set(cache_key, content_data)
            return content_data
        else:
            return {"content": None, "error": "Could not fetch article content"}
    except Exception as e:
        print(f"Error fetching article content: {e}")
        import traceback
        traceback.print_exc()
        return {"content": None, "error": str(e)}

