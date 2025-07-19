"""
Application Configuration
"""
import os
from functools import lru_cache
from typing import Optional, List
from pydantic import BaseSettings, validator


class Settings(BaseSettings):
    """Application settings"""
    
    # App settings
    APP_NAME: str = "1Source API"
    DEBUG: bool = False
    VERSION: str = "1.0.0"
    SECRET_KEY: str = "your-secret-key-here"
    
    # Database
    DATABASE_URL: str = "postgresql://user:pass@localhost/dbname"
    DATABASE_ECHO: bool = False
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379"
    REDIS_RATE_LIMIT_URL: Optional[str] = None
    
    # Rate Limiting
    RATE_LIMIT_DEFAULTS: List[str] = ["60/minute", "2500/hour"]
    RATE_LIMIT_DIVIDER: int = 1
    
    # Azure AD
    AZURE_TENANT_ID: Optional[str] = None
    AZURE_CLIENT_ID: Optional[str] = None
    AZURE_CLIENT_SECRET: Optional[str] = None
    
    # GitHub
    GITHUB_TOKEN: Optional[str] = None
    
    # GraphQL
    GRAPHQL_ENABLED: bool = False
    
    # Proxy settings
    PROXY_HTTP: str = "http://proxy-dmz.intel.com:911"
    PROXY_HTTPS: str = "http://proxy-dmz.intel.com:912"
    NO_PROXY: str = "localhost,127.0.0.1,intel.com"
    
    # Debug
    DEBUG_USER_IDENTIFIER: str = "debug@example.com"
    
    @validator("REDIS_RATE_LIMIT_URL", pre=True)
    def set_redis_rate_limit_url(cls, v, values):
        return v or values.get("REDIS_URL")
    
    class Config:
        env_file = ".env"
        case_sensitive = True


@lru_cache()
def get_settings() -> Settings:
    """Get cached settings instance"""
    return Settings()
