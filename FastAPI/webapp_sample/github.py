"""
GitHub endpoints
"""
from fastapi import APIRouter, Depends, HTTPException
from slowapi import Limiter

from app.core.dependencies import get_limiter
from app.clients.github_client import get_github_client

router = APIRouter()
limiter = get_limiter()


@router.get("/repos")
@limiter.limit("30/minute")
async def get_repositories():
    """Get GitHub repositories"""
    github_client = get_github_client()
    if not github_client:
        raise HTTPException(status_code=503, detail="GitHub client not available")
    
    # Implementation here
    return {"repositories": []}
