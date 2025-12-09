from datetime import datetime, timedelta
from typing import Any, Optional

class Cache:
    def __init__(self, ttl_minutes: int = 12):
        self.cache: dict[str, tuple[Any, datetime]] = {}
        self.ttl = timedelta(minutes=ttl_minutes)
    
    def get(self, key: str) -> Optional[Any]:
        if key not in self.cache:
            return None
        
        value, expiry = self.cache[key]
        if datetime.now() > expiry:
            del self.cache[key]
            return None
        
        return value
    
    def set(self, key: str, value: Any) -> None:
        expiry = datetime.now() + self.ttl
        self.cache[key] = (value, expiry)
    
    def clear(self) -> None:
        self.cache.clear()
    
    def cleanup_expired(self) -> None:
        now = datetime.now()
        expired_keys = [k for k, (_, expiry) in self.cache.items() if now > expiry]
        for key in expired_keys:
            del self.cache[key]

# Global cache instance
cache = Cache(ttl_minutes=12)
