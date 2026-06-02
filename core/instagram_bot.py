"""
Instagram Browser Automation — Human-in-the-Loop.
Opens Chrome, navigates to profile, pastes DM, waits for YOU to click Send.
"""
import os
import time
from playwright.sync_api import sync_playwright
from config.settings import (
    HEADLESS, DISABLE_AUTOMATION_FLAGS, INSTAGRAM_BASE_URL,
    MIN_DM_DELAY, MAX_DM_DELAY
)
from utils.anti_detection import random_viewport, random_user_agent, random_delay, random_typing_delay


class InstagramBot:
    def __init__(self):
        self.browser = None
        self.context = None
        self.page = None

    def start(self):
        """Launch Chrome with Instagram logged in."""
        print("[Bot] Starting Chrome for Instagram automation...")
        p = sync_playwright().start()
        self.browser = p.chromium.launch(
            headless=HEADLESS,
            args=DISABLE_AUTOMATION_FLAGS
        )
        self.context = self.browser.new_context(
            viewport=random_viewport(),
            user_agent=random_user_agent()
        )
        self.page = self.context.new_page()

        # Navigate to Instagram and verify login
        self.page.goto(INSTAGRAM_BASE_URL, wait_until="domcontentloaded", timeout=20000)
        random_delay(3, 5)

        # Check if we're already logged in
        if "login" in self.page.url:
            print("[!] Instagram requires login. Please log in manually in the Chrome window.")
            print("[!] Once logged in, press Enter here to continue...")
            input()
        else:
            print("[Bot] Instagram session active.")

    def send_dm(self, handle, message):
        """
        Navigate to profile, click Message, type message, then WAIT for human approval.
        Returns True if sent, False if skipped.
        """
        profile_url = f"{INSTAGRAM_BASE_URL}/{handle}/"
        print(f"[Bot] Navigating to {profile_url}")

        try:
            self.page.goto(profile_url, wait_until="domcontentloaded", timeout=20000)
            random_delay(2, 4)
        except Exception as e:
            print(f"  [!] Failed to load profile: {e}")
            return False

        # Try to click the Message button
        try:
            # Multiple selector strategies since Instagram changes frequently
            selectors = [
                "svg[aria-label='Messenger']",
                "svg[aria-label='Direct']",
                "button:has-text('Message')",
                "div[role='button']:has-text('Message')",
            ]

            msg_btn = None
            for sel in selectors:
                try:
                    el = self.page.locator(sel).first
                    if el.is_visible(timeout=3000):
                        msg_btn = el
                        break
                except Exception:
                    continue

            if not msg_btn:
                print(f"  [!] Could not find Message button for @{handle}. Skipping.")
                return False

            msg_btn.click()
            random_delay(3, 5)

        except Exception as e:
            print(f"  [!] Error clicking Message button: {e}")
            return False

        # Type the message
        try:
            # Find the textarea/input
            input_selectors = [
                "textarea[placeholder]",
                "div[contenteditable='true']",
                "[role='textbox']",
            ]

            text_input = None
            for sel in input_selectors:
                try:
                    el = self.page.locator(sel).first
                    if el.is_visible(timeout=3000):
                        text_input = el
                        break
                except Exception:
                    continue

            if not text_input:
                print(f"  [!] Could not find message input. Skipping @{handle}.")
                return False

            text_input.click()
            random_delay(1, 2)

            # Type with human-like delays
            text_input.type(message, delay=random_typing_delay())
            random_delay(1, 2)

        except Exception as e:
            print(f"  [!] Error typing message: {e}")
            return False

        # HUMAN IN THE LOOP
        print(f"\n{'='*60}")
        print(f"  READY TO SEND DM to @{handle}")
        print(f"  Message preview:")
        print(f"  \"{message[:200]}{'...' if len(message) > 200 else ''}\"")
        print(f"\n  [ACTION REQUIRED]")
        print(f"  1. Look at the Chrome window — the message is typed.")
        print(f"  2. Review it. Edit if needed.")
        print(f"  3. Press 's' + Enter to confirm SEND")
        print(f"  4. Press 'x' + Enter to SKIP this lead")
        print(f"{'='*60}\n")

        choice = input(f"  Send to @{handle}? (s/x): ").strip().lower()

        if choice == "s":
            try:
                # Try to click send button
                send_selectors = [
                    "button[type='submit']",
                    "svg[aria-label='Send']",
                    "div[role='button']:has-text('Send')",
                ]
                send_btn = None
                for sel in send_selectors:
                    try:
                        el = self.page.locator(sel).first
                        if el.is_visible(timeout=2000):
                            send_btn = el
                            break
                    except Exception:
                        continue

                if send_btn:
                    send_btn.click()
                    print(f"  [Bot] DM sent to @{handle}")
                    random_delay(MIN_DM_DELAY, MAX_DM_DELAY)
                    return True
                else:
                    # If we can't find the button, alert user to click manually
                    print(f"  [!] Could not auto-click Send. Please click the Send button manually.")
                    input("  Press Enter after you've sent the message...")
                    return True

            except Exception as e:
                print(f"  [!] Error sending: {e}")
                return False
        else:
            print(f"  [Bot] Skipped @{handle}")
            return False

    def close(self):
        if self.browser:
            self.browser.close()
            print("[Bot] Browser closed.")
