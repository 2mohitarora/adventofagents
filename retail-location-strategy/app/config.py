import os
from pathlib import Path

from dotenv import load_dotenv

# Load environment variables from .env file in the app directory
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY", "")
MAPS_API_KEY = os.environ.get("MAPS_API_KEY", "")

# Model Configuration
# ============================================================================
# Uncomment the model set you want to use. Only one set should be active.
# NOTE: Gemini 2.5 Pro is RECOMMENDED for stability. Gemini 3 Pro Preview
#       may throw "model overloaded" (503) errors during high-demand periods.
# ============================================================================

# Option 1: Gemini 2.5 Pro (RECOMMENDED - stable, good for production)
#FAST_MODEL = "gemini-2.5-pro"
#PRO_MODEL = "gemini-2.5-pro"
#CODE_EXEC_MODEL = "gemini-2.5-pro"
#IMAGE_MODEL = "gemini-3-pro-image-preview"  # Gemini 3 for native image generation

# Option 2: Gemini 3 Pro Preview (latest features, may have availability issues)
# FAST_MODEL = "gemini-3-pro-preview"
# PRO_MODEL = "gemini-3-pro-preview"
# CODE_EXEC_MODEL = "gemini-3-pro-preview"
# IMAGE_MODEL = "gemini-3-pro-image-preview"

# Option 3: Gemini 2.5 Flash (fastest, lowest cost)
FAST_MODEL = "gemini-2.5-flash"
PRO_MODEL = "gemini-2.5-flash"
CODE_EXEC_MODEL = "gemini-2.5-flash"
IMAGE_MODEL = "gemini-2.0-flash-exp"

# Retry Configuration (for handling model overload errors)
# Note: HttpRetryOptions may only retry on certain HTTP codes (429, etc.)
# For persistent 503 errors, consider using a different model or waiting for API availability
RETRY_INITIAL_DELAY = 5  # seconds - longer wait for overloaded models
RETRY_ATTEMPTS = 5  # More attempts for transient errors
RETRY_MAX_DELAY = 60  # seconds

# App Configuration
APP_NAME = "retail_location_strategy"