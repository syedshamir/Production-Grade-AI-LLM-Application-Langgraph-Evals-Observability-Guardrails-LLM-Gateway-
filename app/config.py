import os
from dotenv import load_dotenv

# Load local development secrets before Settings is instantiated. In deployed
# environments these values can still come from the process environment.
load_dotenv()

class Settings:
    """Centralized environment-backed settings for external services."""

    TAVILY_API_KEY: str = os.getenv("TAVILY_API_KEY")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY")
    GROQ_FALLBACK_API_KEY: str = os.getenv("GROQ_FALLBACK_API_KEY")
    GROQ_MODEL = "llamma-3.3-70b-versatile"  # or "gpt-4o" for the full version
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    QDRANT_COLLECTION_NAME: str = os.getenv("QDRANT_COLLECTION_NAME")
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY")
    QDRANT_CLUSTER_ENDPOINT: str = os.getenv("QDRANT_CLUSTER_ENDPOINT")

# Import this singleton wherever configuration is needed so environment loading
# stays consistent across ingestion, retrieval, and future app entry points.
settings = Settings()
