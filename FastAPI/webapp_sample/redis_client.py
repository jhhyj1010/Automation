"""
Redis Client
"""
import logging
from typing import Optional
import redis
from app.core.config import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)


class RedisClient:
    """Redis client wrapper"""
    
    def __init__(self, url: str):
        self.redis = redis.from_url(url, decode_responses=True)
    
    def ping(self) -> bool:
        """Ping Redis server"""
        try:
            return self.redis.ping()
        except Exception as e:
            logger.error(f"Redis ping failed: {e}")
            return False
    
    def get(self, key: str) -> Optional[str]:
        """Get value by key"""
        try:
            return self.redis.get(key)
        except Exception as e:
            logger.error(f"Redis get failed: {e}")
            return None
    
    def set(self, key: str, value: str, ex: Optional[int] = None) -> bool:
        """Set key-value pair"""
        try:
            return self.redis.set(key, value, ex=ex)
        except Exception as e:
            logger.error(f"Redis set failed: {e}")
            return False


_redis_client: Optional[RedisClient] = None


def get_redis_client() -> Optional[RedisClient]:
    """Get Redis client singleton"""
    global _redis_client
    if _redis_client is None and settings.REDIS_URL:
        try:
            _redis_client = RedisClient(settings.REDIS_URL)
        except Exception as e:
            logger.error(f"Failed to create Redis client: {e}")
    return _redis_client
