"""
Anti-detection utilities for browser automation.
"""
import random
import time


def random_delay(min_sec=30, max_sec=120):
    """Sleep for a random duration between min and max seconds."""
    delay = random.uniform(min_sec, max_sec)
    time.sleep(delay)
    return delay


def random_typing_delay():
    """Return a random per-character typing delay in ms."""
    return random.randint(80, 180)


def jitter_mouse(page):
    """
    Move mouse to a random position on the page to simulate human behavior.
    This is a no-op placeholder — real mouse movement requires more advanced tools.
    """
    try:
        width = page.viewport_size["width"]
        height = page.viewport_size["height"]
        x = random.randint(100, width - 100)
        y = random.randint(100, height - 100)
        page.mouse.move(x, y)
    except Exception:
        pass


def random_viewport():
    """Return a common desktop viewport size."""
    sizes = [
        {"width": 1280, "height": 720},
        {"width": 1366, "height": 768},
        {"width": 1440, "height": 900},
        {"width": 1536, "height": 864},
        {"width": 1920, "height": 1080},
    ]
    return random.choice(sizes)


def random_user_agent():
    """Return a recent Chrome user agent string."""
    agents = [
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    ]
    return random.choice(agents)
