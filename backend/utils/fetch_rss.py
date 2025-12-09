import feedparser
import httpx
import re
from typing import List, Dict, Any
from datetime import datetime
from utils.clean_data import clean_text, parse_date

RSS_FEEDS = [
    {
        "name": "Google News AI",
        "url": "https://news.google.com/rss/search?q=artificial+intelligence+AI&hl=en-US&gl=US&ceid=US:en"
    },
    {
        "name": "TechCrunch AI",
        "url": "https://techcrunch.com/tag/artificial-intelligence/feed/"
    },
    {
        "name": "OpenAI Blog",
        "url": "https://openai.com/blog/rss.xml"
    },
    {
        "name": "DeepMind Blog",
        "url": "https://deepmind.com/blog/feed/basic/"
    },
    {
        "name": "Anthropic Blog",
        "url": "https://www.anthropic.com/index.xml"
    }
]

async def fetch_rss_feed(url: str, source_name: str) -> List[Dict[str, Any]]:
    """Fetch and parse a single RSS feed."""
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            response = await client.get(url)
            response.raise_for_status()
            
            feed = feedparser.parse(response.text)
            articles = []
            
            for entry in feed.entries[:20]:  # Limit to 20 per feed
                article = {
                    "title": clean_text(entry.get("title", "")),
                    "description": clean_text(entry.get("description", "") or entry.get("summary", "")),
                    "link": entry.get("link", ""),
                    "published_at": entry.get("published", ""),
                    "source": source_name,
                    "author": entry.get("author", ""),
                    "image": None
                }
                
                # Try multiple methods to extract image
                image_url = None
                
                # Method 1: Check media_content (RSS 2.0 media tags)
                if hasattr(entry, "media_content") and entry.media_content:
                    for media in entry.media_content:
                        if media.get("type", "").startswith("image"):
                            image_url = media.get("url")
                            break
                
                # Method 2: Check links for image types
                if not image_url and hasattr(entry, "links"):
                    for link in entry.links:
                        if link.get("type", "").startswith("image"):
                            image_url = link.get("href")
                            break
                
                # Method 3: Check for media_thumbnail
                if not image_url and hasattr(entry, "media_thumbnail") and entry.media_thumbnail:
                    image_url = entry.media_thumbnail[0].get("url")
                
                # Method 4: Extract from description/summary HTML
                if not image_url:
                    description = entry.get("description", "") or entry.get("summary", "")
                    if description:
                        # Look for img tags
                        img_match = re.search(r'<img[^>]+src=["\']([^"\']+)["\']', description, re.IGNORECASE)
                        if img_match:
                            image_url = img_match.group(1)
                        # Look for background-image in style
                        if not image_url:
                            bg_match = re.search(r'background-image:\s*url\(["\']?([^"\']+)["\']?\)', description, re.IGNORECASE)
                            if bg_match:
                                image_url = bg_match.group(1)
                
                # Method 5: Check feed-level image
                if not image_url and hasattr(feed, "image") and feed.image:
                    image_url = feed.image.get("href")
                
                # Method 6: Use a unique AI-themed placeholder based on article title
                if not image_url:
                    # List of AI/tech themed Unsplash images
                    ai_images = [
                        "https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=600&fit=crop",  # AI brain
                        "https://images.unsplash.com/photo-1485827404703-89b55fcc595e?w=800&h=600&fit=crop",  # Neural network
                        "https://images.unsplash.com/photo-1555255707-c07966088b7b?w=800&h=600&fit=crop",  # AI robot
                        "https://images.unsplash.com/photo-1488590528505-98d2b5aba04b?w=800&h=600&fit=crop",  # Tech circuit
                        "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&h=600&fit=crop",  # AI chip
                        "https://images.unsplash.com/photo-1504639725590-34d0984388bd?w=800&h=600&fit=crop",  # Code/AI
                        "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&h=600&fit=crop",  # Digital world
                        "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=600&fit=crop",  # AI visualization
                        "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&h=600&fit=crop",  # Machine learning
                        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",  # Tech innovation
                        "https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=600&fit=crop",  # AI data
                        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",  # Analytics
                        "https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=800&h=600&fit=crop",  # AI network
                        "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?w=800&h=600&fit=crop",  # Innovation
                        "https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=600&fit=crop",  # Data science
                    ]
                    
                    # Generate a consistent index based on article title
                    title_hash = hash(article.get("title", ""))
                    image_index = abs(title_hash) % len(ai_images)
                    image_url = ai_images[image_index]
                
                article["image"] = image_url
                
                # Parse date
                if article["published_at"]:
                    article["published_at"] = parse_date(article["published_at"]).isoformat()
                else:
                    article["published_at"] = datetime.now().isoformat()
                
                if article["title"]:
                    articles.append(article)
            
            return articles
    except Exception as e:
        print(f"Error fetching RSS feed {url}: {e}")
        return []

async def fetch_all_rss_feeds() -> List[Dict[str, Any]]:
    """Fetch all RSS feeds concurrently."""
    import asyncio
    
    tasks = [fetch_rss_feed(feed["url"], feed["name"]) for feed in RSS_FEEDS]
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    all_articles = []
    for result in results:
        if isinstance(result, list):
            all_articles.extend(result)
        elif isinstance(result, Exception):
            print(f"Error in RSS fetch: {result}")
    
    return all_articles

