"""
OpenRouter AI analyzer.
Calls Kimi K2 or Gemini Flash for website audits and DM copy.
"""
import requests
import json
import time
from config.settings import OPENROUTER_API_KEY, DEFAULT_MODEL, FALLBACK_MODEL, OPENROUTER_DELAY
from utils.rate_limiter import RateLimiter

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

class AIAnalyzer:
    def __init__(self):
        self.api_key = OPENROUTER_API_KEY
        self.primary_model = DEFAULT_MODEL
        self.fallback_model = FALLBACK_MODEL
        self.rate_limiter = RateLimiter(rpm=20)
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://outworld.local",
            "X-Title": "Outworld Lead Engine"
        }

    def _call(self, prompt, model=None, max_retries=2):
        if not self.api_key:
            raise ValueError("OPENROUTER_API_KEY not set in .env")

        self.rate_limiter.wait()

        payload = {
            "model": model or self.primary_model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
            "max_tokens": 1200
        }

        for attempt in range(max_retries):
            try:
                resp = requests.post(BASE_URL, headers=self.headers, json=payload, timeout=60)
                data = resp.json()

                if resp.status_code == 429:
                    # Rate limited — fallback to other model
                    print(f"  [!] Rate limited on {payload['model']}, trying fallback...")
                    payload["model"] = self.fallback_model
                    self.rate_limiter.wait()
                    continue

                if "choices" in data and len(data["choices"]) > 0:
                    return data["choices"][0]["message"]["content"]

                if "error" in data:
                    print(f"  [!] API error: {data['error']}")
                    if attempt < max_retries - 1:
                        payload["model"] = self.fallback_model
                        self.rate_limiter.wait()
                        continue

            except Exception as e:
                print(f"  [!] Request failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5)
                    continue

        return "[AI analysis unavailable — check API key or rate limits]"

    def analyze_website(self, prompt):
        """Run the website audit prompt."""
        print(f"  [AI] Analyzing with {self.primary_model}...")
        return self._call(prompt)

    def generate_dm(self, prompt):
        """Generate a DM variant."""
        return self._call(prompt, max_retries=1)
