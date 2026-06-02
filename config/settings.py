"""
Global settings for Outworld Creative — Creative Director Branch.
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
DOCS_DIR = os.path.join(BASE_DIR, "docs")
LANDING_DIR = os.path.join(BASE_DIR, "landing_page")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

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

# Company Info
COMPANY_NAME = "Outworld Creative"
COMPANY_TAGLINE = "Video Ads and Brand Sound"
COMPANY_CONTACT = "team@outworldcreative.com"
COMPANY_WEBSITE = "https://outworldcreative.com"

# Brand Colors
BRAND_PRIMARY_COLOR = (0.05, 0.05, 0.05)       # near-black
BRAND_ACCENT_COLOR = (0.95, 0.25, 0.25)          # deep red
BRAND_TEXT_COLOR = (0.2, 0.2, 0.2)
BRAND_LIGHT_BG = (0.97, 0.97, 0.97)

# Internal Pricing (never shown publicly)
CREATIVE_DIAGNOSIS_PRICE_RANGE = "R1,500 - R3,500"
MONTHLY_RETAINER_RANGE = "R8,000 - R20,000"
CAMPAIGN_STRATEGY_RANGE = "R15,000 - R40,000"

# Kie.ai Settings
KIE_API_KEY = os.getenv("KIE_API_KEY", "")
KIE_BASE_URL = "https://api.kie.ai/v1"
KIE_IMAGE_MODEL = "google/nano-banana-2"
KIE_VIDEO_MODEL = "seedance-1-5-pro"

# Spec Ad Lab
SPEC_AD_LAB_DIR = os.path.join(ASSETS_DIR, "spec-lab")
ANIMATED_ADS = [1, 4, 7]  # Campaign numbers to animate

# Outreach
OUTREACH_CHANNELS = ["instagram_dm", "linkedin", "cold_email"]
OUTREACH_TARGETS_PER_NICHE = 10
FOLLOW_UP_DAYS = [3, 7, 14]

# Discovery Call
DISCOVERY_CALL_DURATION_MIN = 20
DISCOVERY_CALL_DURATION_MAX = 30
PROPOSAL_DELIVERY_HOURS = 48

# Signal Desk Content Engine
SIGNAL_DESK_PILLARS = [
    "creative_intelligence",
    "ad_breakdowns",
    "brand_sound",
    "creator_economy_news",
    "industry_opportunities",
    "savehxpe_notes",
    "spec_ad_lab_drops",
    "remote_studio_build",
    "comparison_desk"
]
SIGNAL_DESK_DAILY_POSTS = 2  # 1 X post + 1 Instagram carousel
SIGNAL_DESK_SOFT_CTAS = [
    "Outworld is building for this.",
    "This is why brands need creative direction, not just content.",
    "Request a Creative Diagnosis.",
    "Most brands have a look. Very few have a sound.",
    "Built from Africa. Designed for the world.",
    "Stop using random sounds for serious ads.",
    "A strong ad needs three things: a hook, a visual, and a sound people remember.",
    "We make ads that look good, sound right, and sell the idea fast."
]

# Logo Carousel Assets (local saveHXPE directory)
LOGO_PARTNER_DIR = "/Users/tshepomotolo/seohxpe/public/brand/partners"
LOGO_APPEARANCE_DIR = "/Users/tshepomotolo/seohxpe/public/brand/appearances"
LOGO_OUTWORLD_PATH = "/Users/tshepomotolo/seohxpe/public/brand/logos/outworld_logo.webp"

PARTNER_LOGOS = [
    ("Adidas", "adidas/Adidas_logo.webp"),
    ("Sportscene", "sportscene/sportscene_logo.webp"),
    ("KFC", "kfc/KFC_logo.webp"),
    ("Empire", "empire/Empire_Distribution_logo.webp"),
    ("STEM", "stem/stem_logo.webp"),
    ("Radical", "radical/radical_logo.webp"),
    ("SinceThe80s", "since-the-80s/sincethe80s_logo.webp"),
    ("365", "365/365_logo.webp"),
]

APPEARANCE_LOGOS = [
    ("MTV", "mtv/Mtv.webp"),
    ("News24", "news24/News24.webp"),
    ("SABC", "sabc/SABC-channel-africa.webp"),
    ("OkayAfrica", "okayafrica/OkayAfrica.webp"),
    ("Channel O", "channelO/Channel-o.webp"),
    ("Trace", "trace/trace.webp"),
    ("HNHH", "hnhh/hnhh.webp"),
]
