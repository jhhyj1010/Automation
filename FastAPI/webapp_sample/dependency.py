"""
Application Dependencies
"""
import logging
from typing import Optional
from fastapi import Request, Header
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.core.config import get_settings
from app.clients.redis_client import get_redis_client

settings = get_settings()
logger = logging.getLogger(__name__)


def get_user_identifier(request: Request) -> str:
    """Get user identifier for rate limiting"""
    intel_email = request.headers.get("Intel-Email")
    intel_idsid = request.headers.get("Intel-Idsid")
    
    if intel_email:
        return intel_email
    elif intel_idsid:
        return intel_idsid
    else:
        return settings.DEBUG_USER_IDENTIFIER or get_remote_address(request)


def get_limiter() -> Limiter:
    """Get rate limiter instance"""
    redis_client = get_redis_client()
    
    if redis_client and redis_client.ping():
        storage_uri = settings.REDIS_RATE_LIMIT_URL
    else:
        storage_uri = "memory://"
        logger.warning("Redis not available, using memory storage for rate limiting")
    
    return Limiter(
        key_func=get_user_identifier,
        storage_uri=storage_uri,
        application_limits=settings.RATE_LIMIT_DEFAULTS
    )
