"""
Google Lighthouse CLI wrapper.
Runs a local Lighthouse audit and returns structured JSON.
Requires: npm install -g lighthouse (or use npx)
"""
import subprocess
import json
import os
import tempfile


class LighthouseAuditor:
    def __init__(self):
        self.device = "mobile"

    def run(self, url):
        """
        Run Lighthouse on the given URL.
        Returns: dict with scores and flags.
        """
        print(f"  [Lighthouse] Auditing: {url}")

        output_file = os.path.join(tempfile.gettempdir(), f"lh_{abs(hash(url))}.json")

        cmd = [
            "lighthouse",
            url,
            f"--preset={self.device}",
            "--output=json",
            f"--output-path={output_file}",
            "--chrome-flags=--headless",
            "--only-categories=performance",
            "--only-categories=accessibility",
            "--only-categories=best-practices",
            "--only-categories=seo"
        ]

        try:
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
            if not os.path.exists(output_file):
                print(f"  [!] Lighthouse failed: {result.stderr[:200]}")
                return self._empty_result()

            with open(output_file, "r") as f:
                data = json.load(f)

            os.remove(output_file)
            return self._parse(data)

        except FileNotFoundError:
            print("  [!] Lighthouse CLI not found. Install with: npm install -g lighthouse")
            return self._empty_result()
        except subprocess.TimeoutExpired:
            print("  [!] Lighthouse timed out")
            return self._empty_result()
        except Exception as e:
            print(f"  [!] Lighthouse error: {e}")
            return self._empty_result()

    def _parse(self, data):
        categories = data.get("categories", {})
        scores = {}
        flags = []

        for key in ["performance", "accessibility", "best-practices", "seo"]:
            cat = categories.get(key)
            if cat:
                score = int(cat["score"] * 100)
                scores[key] = score
                if score < 50:
                    flags.append(f"{key}_critical")
                elif score < 70:
                    flags.append(f"{key}_poor")
            else:
                scores[key] = 0
                flags.append(f"{key}_missing")

        # Check for mobile responsiveness via audits
        audits = data.get("audits", {})
        viewport_audit = audits.get("viewport", {})
        if not viewport_audit.get("score"):
            flags.append("mobile_viewport_issue")

        return {"scores": scores, "flags": flags}

    def _empty_result(self):
        return {
            "scores": {
                "performance": 0,
                "accessibility": 0,
                "best-practices": 0,
                "seo": 0
            },
            "flags": ["audit_failed"]
        }
