"""
Status endpoints
"""
from fastapi import APIRouter, Depends
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.core.dependencies import get_limiter

router = APIRouter()
limiter = get_limiter()


@router.get("/health")
@limiter.limit("60/minute")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "1source-api"}


@router.get("/")
@limiter.limit("60/minute")
async def status():
    """Status endpoint"""
    return {"status": "ok", "version": "1.0.0"}
