"""
DM Copywriter.
Generates 3 DM variants using AI prompts.
"""
import os
from prompts.dm_prompts import build_dm_prompts
from core.ai_analyzer import AIAnalyzer
from config.settings import OUTREACH_DIR
from config.niches import get_niche_config


class DMCopywriter:
    def __init__(self):
        self.ai = AIAnalyzer()
        os.makedirs(OUTREACH_DIR, exist_ok=True)

    def generate(self, handle, niche_key, audit_summary, website_found, service_pitch):
        """
        Generate 3 DM variants and save them to a file.
        Returns: path to the outreach file.
        """
        niche_config = get_niche_config(niche_key)
        prompts = build_dm_prompts(handle, niche_config, audit_summary, website_found, service_pitch)

        variants = {}
        for variant_name, prompt in prompts.items():
            print(f"  [Copywriter] Generating '{variant_name}' DM...")
            text = self.ai.generate_dm(prompt)
            variants[variant_name] = text.strip()

        # Save to file
        outreach_path = os.path.join(OUTREACH_DIR, f"{handle}_dm.txt")
        with open(outreach_path, "w", encoding="utf-8") as f:
            f.write(f"Outreach DMs for @{handle}\n")
            f.write(f"Niche: {niche_config['name']}\n")
            f.write(f"Website found: {'Yes' if website_found else 'No'}\n")
            f.write("=" * 50 + "\n\n")

            for variant_name, text in variants.items():
                f.write(f"--- VARIANT: {variant_name.upper()} ---\n")
                f.write(text + "\n\n")

        print(f"  [Copywriter] Saved outreach: {outreach_path}")
        return outreach_path, variants
