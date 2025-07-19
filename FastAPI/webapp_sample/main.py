"""
FastAPI Application Entry Point
"""
import logging
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.core.config import get_settings
from app.core.database import get_database_manager
from app.core.logging_config import setup_logging
from app.api.v1.api import api_router
from app.core.exceptions import setup_exception_handlers
from app.core.middleware import setup_middleware
from app.core.dependencies import get_limiter

settings = get_settings()
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    """Application lifespan events"""
    # Startup
    logger.info("Starting FastAPI application...")
    setup_logging()
    
    # Initialize database
    db_manager = get_database_manager()
    await db_manager.initialize()
    
    # Initialize Redis for rate limiting
    limiter = get_limiter()
    
    logger.info("FastAPI application started successfully")
    
    yield
    
    # Shutdown
    logger.info("Shutting down FastAPI application...")
    await db_manager.close()
    logger.info("FastAPI application shutdown complete")


def create_app() -> FastAPI:
    """Create FastAPI application"""
    
    app = FastAPI(
        title="1Source API",
        description="1Source FastAPI Application",
        version="1.0.0",
        docs_url="/docs" if settings.DEBUG else None,
        redoc_url="/redoc" if settings.DEBUG else None,
        openapi_url="/openapi.json" if settings.DEBUG else None,
        lifespan=lifespan
    )
    
    # Setup middleware
    setup_middleware(app)
    
    # Setup exception handlers
    setup_exception_handlers(app)
    
    # Rate limiting
    limiter = get_limiter()
    app.state.limiter = limiter
    app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
    app.add_middleware(SlowAPIMiddleware)
    
    # Include routers
    app.include_router(api_router, prefix="/api")
    
    return app


# Create the app instance
app = create_app()
