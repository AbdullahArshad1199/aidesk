from datetime import datetime
from typing import List, Dict, Any
import re
from collections import Counter

def clean_text(text: str) -> str:
    """Clean and normalize text content."""
    if not text:
        return ""
    # Remove HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def parse_date(date_str: str) -> datetime:
    """Parse various date formats to datetime."""
    if not date_str:
        return datetime.now()
    
    # Handle datetime objects
    if isinstance(date_str, datetime):
        return date_str
    
    # Handle already parsed ISO strings
    if isinstance(date_str, str) and 'T' in date_str:
        try:
            # Try parsing ISO format directly
            from dateutil import parser
            return parser.parse(date_str)
        except:
            pass
    
    # Common RSS date formats
    formats = [
        "%a, %d %b %Y %H:%M:%S %z",
        "%a, %d %b %Y %H:%M:%S %Z",
        "%Y-%m-%dT%H:%M:%S%z",
        "%Y-%m-%dT%H:%M:%S",
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d",
    ]
    
    for fmt in formats:
        try:
            parsed = datetime.strptime(str(date_str), fmt)
            return parsed
        except:
            continue
    
    # Fallback: try dateutil parser
    try:
        from dateutil import parser
        return parser.parse(str(date_str))
    except:
        pass
    
    return datetime.now()

def deduplicate_articles(articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Remove duplicate articles based on title similarity."""
    seen_titles = set()
    unique_articles = []
    
    for article in articles:
        title = article.get("title", "").lower().strip()
        # Normalize title for comparison
        title_normalized = re.sub(r'[^\w\s]', '', title)
        
        # Check if similar title exists
        is_duplicate = False
        for seen_title in seen_titles:
            # Simple similarity check
            if title_normalized in seen_title or seen_title in title_normalized:
                if len(title_normalized) > 20 and len(seen_title) > 20:
                    is_duplicate = True
                    break
        
        if not is_duplicate:
            seen_titles.add(title_normalized)
            unique_articles.append(article)
    
    return unique_articles

def extract_keywords(text: str) -> List[str]:
    """Extract important keywords from text."""
    if not text:
        return []
    
    text_lower = text.lower()
    keywords = []
    
    important_terms = [
        "agi", "artificial general intelligence", "gpt", "llm", "model release",
        "breakthrough", "announcement", "research", "ai bill", "safety",
        "openai", "deepmind", "anthropic", "claude", "gemini", "chatgpt"
    ]
    
    for term in important_terms:
        if term in text_lower:
            keywords.append(term)
    
    return keywords

def categorize_article(article: Dict[str, Any], all_articles: List[Dict[str, Any]]) -> Dict[str, bool]:
    """Categorize article as trending or important."""
    try:
        title = str(article.get("title", "")).lower()
        description = str(article.get("description", "")).lower()
        content = f"{title} {description}"
        
        publish_date = article.get("published_at")
        if isinstance(publish_date, str):
            try:
                publish_date = parse_date(publish_date)
            except:
                publish_date = datetime.now()
        elif not isinstance(publish_date, datetime):
            publish_date = datetime.now()
        
        # Check if trending (last 24 hours - more lenient)
        is_trending = False
        if publish_date:
            try:
                # Handle timezone-aware datetimes
                if publish_date.tzinfo is not None:
                    from datetime import timezone
                    now = datetime.now(timezone.utc)
                    hours_ago = (now - publish_date).total_seconds() / 3600
                else:
                    hours_ago = (datetime.now() - publish_date).total_seconds() / 3600
                # More lenient: last 24 hours instead of 12
                if hours_ago <= 24:
                    is_trending = True
            except Exception as e:
                print(f"Error calculating hours ago: {e}")
                pass
    
        # Check if appears in multiple sources
        title_normalized = re.sub(r'[^\w\s]', '', title)
        source_count = sum(1 for a in all_articles 
                          if re.sub(r'[^\w\s]', '', str(a.get("title", "")).lower()) == title_normalized)
        if source_count > 1:
            is_trending = True
        
        # Viral keywords
        viral_keywords = ["breaking", "exclusive", "major", "huge", "revolutionary", "new", "latest", "update", "announcement"]
        if any(kw in content for kw in viral_keywords):
            is_trending = True
        
        # Check if important
        is_important = False
        important_keywords = [
            "model release", "agi", "breakthrough", "announcement", 
            "research", "ai bill", "safety", "gpt-", "claude", "gemini"
        ]
        
        if any(kw in content for kw in important_keywords):
            is_important = True
        
        # Check if from major labs
        source = str(article.get("source", "")).lower()
        major_labs = ["openai", "deepmind", "anthropic", "google research"]
        if any(lab in source for lab in major_labs):
            is_important = True
        
        return {
            "trending": is_trending,
            "important": is_important
        }
    except Exception as e:
        print(f"Error categorizing article: {e}")
        return {
            "trending": False,
            "important": False
        }

