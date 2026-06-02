"""
Global settings for Outworld Lead Engine.
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
BATCHES_DIR = os.path.join(DATA_DIR, "batches")
OUTPUT_DIR = os.path.join(BASE_DIR, "output")
AUDITS_DIR = os.path.join(OUTPUT_DIR, "audits")
OUTREACH_DIR = os.path.join(OUTPUT_DIR, "outreach")
DB_PATH = os.path.join(DATA_DIR, "leads.db")

# API Keys
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
DEFAULT_MODEL = os.getenv("DEFAULT_MODEL", "kimi/k2")
FALLBACK_MODEL = os.getenv("FALLBACK_MODEL", "google/gemini-flash-1.5")

# Rate Limiting
OPENROUTER_RPM = 20  # requests per minute
OPENROUTER_DELAY = 60.0 / OPENROUTER_RPM  # seconds between requests

# Instagram Automation
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "livesavehxpe")
INSTAGRAM_BASE_URL = "https://www.instagram.com"
DM_DAILY_LIMIT = 30  # Instagram's soft limit for non-follower DMs
MIN_DM_DELAY = 45     # seconds
MAX_DM_DELAY = 120    # seconds

# Playwright / Browser
HEADLESS = False  # Must be False for human-in-the-loop
CHROME_USER_DATA_DIR = os.getenv("CHROME_USER_DATA_DIR", "")
DISABLE_AUTOMATION_FLAGS = [
    "--disable-blink-features=AutomationControlled",
    "--disable-web-security",
    "--disable-features=IsolateOrigins,site-per-process",
]

# Lighthouse
LIGHTHOUSE_CATEGORIES = ["performance", "accessibility", "best-practices", "seo"]
LIGHTHOUSE_DEVICE = "mobile"

# PDF Generation
COMPANY_NAME = "Outworld"
COMPANY_TAGLINE = "Web Design & Digital Growth"
COMPANY_CONTACT = "DM @livesavehxpe or reply here"
BRAND_PRIMARY_COLOR = (0.12, 0.12, 0.12)       # near-black
BRAND_ACCENT_COLOR = (0.85, 0.20, 0.20)          # deep red
BRAND_TEXT_COLOR = (0.2, 0.2, 0.2)
BRAND_LIGHT_BG = (0.97, 0.97, 0.97)
