"""
AI prompts for website audit analysis.
These are sent to OpenRouter (Kimi K2 or Gemini Flash).
"""


def build_audit_prompt(screenshot_description, lighthouse_json, niche, handle):
    """
    Build the prompt for AI website critique.
    screenshot_description: text description of what the scraper saw (or a placeholder)
    lighthouse_json: dict of Lighthouse scores
    niche: 'musician' or 'clothing_brand'
    handle: Instagram handle
    """
    scores = lighthouse_json.get("scores", {})
    score_text = "\n".join([f"- {k.replace('-', ' ').title()}: {v}/100" for k, v in scores.items()])

    flags = lighthouse_json.get("flags", [])
    flags_text = "\n".join([f"- {f}" for f in flags]) if flags else "- No major flags detected"

    prompt = f"""You are a senior web design and digital marketing consultant. Your client is a South African creative entrepreneur.

You have just analyzed the website of an Instagram account: @{handle}
Niche: {niche.replace('_', ' ').title()}

Here are the Lighthouse performance scores:
{score_text}

Detected issues / flags:
{flags_text}

Please provide a concise but professional audit report with the following sections:

1. **First Impression** (2-3 sentences on visual design, branding, clarity)
2. **Mobile Experience** (is it usable on phone? common issues)
3. **Performance** (are load times hurting visitors?)
4. **SEO & Discoverability** (will Google find them?)
5. **Missing Features** (what should a {niche.replace('_', ' ')} site have that this one lacks?)
6. **Priority Fixes** (top 3 things to fix, ranked by impact)
7. **Recommendation** (should they rebuild, refresh, or just optimize? suggest the service tier)

Keep it actionable. Use plain language. The reader is not technical.
"""
    return prompt.strip()


def build_no_website_prompt(handle, niche, bio_text):
    """Build prompt when no website is found."""
    prompt = f"""You are a web design consultant analyzing an Instagram presence.

Account: @{handle}
Niche: {niche.replace('_', ' ').title()}
Bio snippet: {bio_text or 'No bio available'}

This account does NOT have a website linked in their bio.

Please write a brief "Missed Opportunity Analysis" with these sections:

1. **The Problem** (why not having a website hurts their specific niche)
2. **What They're Losing** (bookings? sales? credibility? fan engagement?)
3. **What a Website Would Fix** (3 concrete benefits tailored to this niche)
4. **Quick Win Recommendation** (suggest a simple 3-5 page site structure)

Keep it persuasive but not pushy. The tone should be expert but friendly.
"""
    return prompt.strip()
