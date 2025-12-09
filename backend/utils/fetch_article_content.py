import httpx
from typing import Optional, Dict, Any
import re
from bs4 import BeautifulSoup

async def fetch_article_content(url: str) -> Optional[Dict[str, Any]]:
    """Fetch full article content from the source URL."""
    try:
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True) as client:
            # Set headers to mimic a browser
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            }
            
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            
            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Try to find article content using common selectors
            content = None
            
            # Common article content selectors
            selectors = [
                'article',
                '[role="article"]',
                '.article-content',
                '.post-content',
                '.entry-content',
                '.content',
                'main article',
                '.article-body',
                '.post-body',
            ]
            
            for selector in selectors:
                element = soup.select_one(selector)
                if element:
                    # Remove script and style elements
                    for script in element(["script", "style", "nav", "aside", "footer", "header"]):
                        script.decompose()
                    
                    # Get text content
                    content = element.get_text(separator='\n\n', strip=True)
                    if len(content) > 200:  # Ensure we have substantial content
                        break
            
            # If no content found, try to get body text
            if not content or len(content) < 200:
                body = soup.find('body')
                if body:
                    # Remove unwanted elements
                    for unwanted in body(["script", "style", "nav", "aside", "footer", "header", "iframe"]):
                        unwanted.decompose()
                    content = body.get_text(separator='\n\n', strip=True)
            
            # Clean up content
            if content:
                # Remove excessive whitespace
                content = re.sub(r'\n{3,}', '\n\n', content)
                content = re.sub(r' {2,}', ' ', content)
                content = content.strip()
            
            # Get article title if available
            title = None
            title_selectors = ['h1', 'title', '.article-title', '.post-title', '.entry-title']
            for selector in title_selectors:
                element = soup.select_one(selector)
                if element:
                    title = element.get_text(strip=True)
                    if title:
                        break
            
            return {
                "content": content,
                "title": title,
                "url": url
            }
            
    except Exception as e:
        print(f"Error fetching article content from {url}: {e}")
        return None

