"""
API Router
"""
from fastapi import APIRouter

from app.api.v1.endpoints import (
    status,
    github,
    feed,
    inventory,
    users,
    vaults
)

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(status.router, prefix="/status", tags=["status"])
api_router.include_router(github.router, prefix="/github", tags=["github"])
api_router.include_router(feed.router, prefix="/feed", tags=["feed"])
api_router.include_router(inventory.router, prefix="/inventory", tags=["inventory"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(vaults.router, prefix="/vaults", tags=["vaults"])
