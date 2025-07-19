"""
GitHub Client
"""
import logging
from typing import Optional
from app.core.config import get_settings

settings = get_settings()
logger = logging.getLogger(__name__)


class GitHubClient:
    """GitHub API Client"""
    
    def __init__(self, token: str):
        self.token = token
        # Initialize GitHub client here
    
    async def get_repositories(self):
        """Get repositories"""
        # Implementation here
        pass


_github_client: Optional[GitHubClient] = None


def get_github_client() -> Optional[GitHubClient]:
    """Get GitHub client singleton"""
    global _github_client
    if _github_client is None and settings.GITHUB_TOKEN:
        _github_client = GitHubClient(settings.GITHUB_TOKEN)
    return _github_client
