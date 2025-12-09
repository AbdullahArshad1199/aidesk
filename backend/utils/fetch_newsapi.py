import os
import httpx
from typing import List, Dict, Any, Optional
from datetime import datetime
from utils.clean_data import clean_text, parse_date

NEWSAPI_KEY = os.getenv("NEWSAPI_KEY", "")
BING_API_KEY = os.getenv("BING_API_KEY", "")

async def fetch_newsapi() -> List[Dict[str, Any]]:
    """Fetch from NewsAPI (optional)."""
    if not NEWSAPI_KEY:
        return []
    
    try:
        url = "https://newsapi.org/v2/everything"
        params = {
            "q": "artificial intelligence OR AI OR machine learning",
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": 50,
            "apiKey": NEWSAPI_KEY
        }
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            
            articles = []
            for item in data.get("articles", []):
                # Get image or use unique default based on title
                image_url = item.get("urlToImage")
                if not image_url:
                    ai_images = [
                        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1555255707-c07966088b7b?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",
                    ]
                    title = item.get("title", "")
                    title_hash = hash(title)
                    image_index = abs(title_hash) % len(ai_images)
                    image_url = ai_images[image_index]
                
                article = {
                    "title": clean_text(item.get("title", "")),
                    "description": clean_text(item.get("description", "")),
                    "link": item.get("url", ""),
                    "published_at": item.get("publishedAt", ""),
                    "source": item.get("source", {}).get("name", "NewsAPI"),
                    "author": item.get("author", ""),
                    "image": image_url
                }
                
                if article["published_at"]:
                    article["published_at"] = parse_date(article["published_at"]).isoformat()
                else:
                    article["published_at"] = datetime.now().isoformat()
                
                if article["title"]:
                    articles.append(article)
            
            return articles
    except Exception as e:
        print(f"Error fetching NewsAPI: {e}")
        return []

async def fetch_bing_news() -> List[Dict[str, Any]]:
    """Fetch from Bing News API (optional)."""
    if not BING_API_KEY:
        return []
    
    try:
        url = "https://api.bing.microsoft.com/v7.0/news/search"
        headers = {"Ocp-Apim-Subscription-Key": BING_API_KEY}
        params = {
            "q": "artificial intelligence AI",
            "count": 50,
            "freshness": "Day"
        }
        
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            data = response.json()
            
            articles = []
            for item in data.get("value", []):
                # Get image or use unique default based on title
                image_url = None
                if item.get("image"):
                    image_url = item.get("image", {}).get("thumbnail", {}).get("content")
                if not image_url:
                    ai_images = [
                        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1555255707-c07966088b7b?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",
                        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",
                    ]
                    title = item.get("name", "")
                    title_hash = hash(title)
                    image_index = abs(title_hash) % len(ai_images)
                    image_url = ai_images[image_index]
                
                article = {
                    "title": clean_text(item.get("name", "")),
                    "description": clean_text(item.get("description", "")),
                    "link": item.get("url", ""),
                    "published_at": item.get("datePublished", ""),
                    "source": item.get("provider", [{}])[0].get("name", "Bing News") if item.get("provider") else "Bing News",
                    "author": "",
                    "image": image_url
                }
                
                if article["published_at"]:
                    article["published_at"] = parse_date(article["published_at"]).isoformat()
                else:
                    article["published_at"] = datetime.now().isoformat()
                
                if article["title"]:
                    articles.append(article)
            
            return articles
    except Exception as e:
        print(f"Error fetching Bing News: {e}")
        return []

async def fetch_all_news_apis() -> List[Dict[str, Any]]:
    """Fetch from all news APIs."""
    import asyncio
    
    tasks = [fetch_newsapi(), fetch_bing_news()]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    all_articles = []
    for result in results:
        if isinstance(result, list):
            all_articles.extend(result)
        elif isinstance(result, Exception):
            print(f"Error in API fetch: {result}")
    
    return all_articles

