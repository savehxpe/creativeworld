"""
Rate limiter for OpenRouter API.
Ensures we stay under 20 RPM on the free tier.
"""
import time
import threading

class RateLimiter:
    def __init__(self, rpm=20):
        self.min_interval = 60.0 / rpm
        self.last_request_time = 0
        self.lock = threading.Lock()

    def wait(self):
        with self.lock:
            now = time.time()
            elapsed = now - self.last_request_time
            if elapsed < self.min_interval:
                sleep_time = self.min_interval - elapsed
                time.sleep(sleep_time)
            self.last_request_time = time.time()
