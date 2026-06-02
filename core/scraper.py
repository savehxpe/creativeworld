"""
Web scraper: Instagram bio extraction + website screenshot.
Uses Playwright.
"""
import os
from playwright.sync_api import sync_playwright
from config.settings import HEADLESS, DISABLE_AUTOMATION_FLAGS
from utils.anti_detection import random_viewport, random_user_agent, random_delay


class WebScraper:
    def __init__(self):
        self.screenshots_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "output", "screenshots")
        os.makedirs(self.screenshots_dir, exist_ok=True)

    def scrape_instagram_bio(self, handle):
        """
        Scrape Instagram profile to extract website URL from bio.
        Returns: dict with {website_url, bio_text, full_name}
        """
        url = f"https://www.instagram.com/{handle}/"
        print(f"  [Scraper] Loading Instagram: {url}")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS, args=DISABLE_AUTOMATION_FLAGS)
            context = browser.new_context(
                viewport=random_viewport(),
                user_agent=random_user_agent()
            )
            page = context.new_page()

            try:
                page.goto(url, wait_until="domcontentloaded", timeout=15000)
                random_delay(2, 4)

                # Try to extract bio text
                bio_text = ""
                try:
                    # Instagram structure changes, but these are common selectors
                    bio_el = page.locator("h1").first.inner_text(timeout=3000)
                    bio_text = bio_el
                except Exception:
                    pass

                # Try to extract website link
                website_url = None
                try:
                    # Look for external link in bio
                    links = page.locator("a[href^='http']").all()
                    for link in links:
                        href = link.get_attribute("href")
                        if href and "instagram.com" not in href and "help.instagram.com" not in href:
                            website_url = href
                            break
                except Exception:
                    pass

                # Also check the specific bio link element
                if not website_url:
                    try:
                        bio_link = page.locator("a[rel='me']").first
                        website_url = bio_link.get_attribute("href")
                    except Exception:
                        pass

                browser.close()
                return {
                    "website_url": website_url,
                    "bio_text": bio_text,
                    "full_name": handle
                }

            except Exception as e:
                print(f"  [!] Failed to scrape Instagram: {e}")
                browser.close()
                return {"website_url": None, "bio_text": "", "full_name": handle}

    def capture_website(self, url, handle):
        """
        Load a website and capture a full-page screenshot + basic HTML text.
        Returns: dict with {screenshot_path, page_title, text_content}
        """
        print(f"  [Scraper] Capturing website: {url}")
        screenshot_path = os.path.join(self.screenshots_dir, f"{handle}_website.png")

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=HEADLESS, args=DISABLE_AUTOMATION_FLAGS)
            context = browser.new_context(
                viewport={"width": 1280, "height": 900},
                user_agent=random_user_agent()
            )
            page = context.new_page()

            try:
                page.goto(url, wait_until="networkidle", timeout=20000)
                random_delay(3, 5)

                page.screenshot(path=screenshot_path, full_page=True)
                title = page.title()

                # Extract visible text
                text_content = ""
                try:
                    text_content = page.inner_text("body", timeout=5000)
                    # Truncate to avoid memory issues
                    text_content = text_content[:3000]
                except Exception:
                    pass

                browser.close()
                return {
                    "screenshot_path": screenshot_path,
                    "page_title": title,
                    "text_content": text_content
                }

            except Exception as e:
                print(f"  [!] Failed to capture website: {e}")
                browser.close()
                return {
                    "screenshot_path": None,
                    "page_title": "",
                    "text_content": ""
                }
