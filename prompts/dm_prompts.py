"""
AI prompts for DM copywriting.
Generates 3 variants per lead.
"""


def build_dm_prompts(handle, niche_config, audit_summary, website_found, service_pitch):
    """
    Build prompts for 3 DM variants.
    Returns a dict with keys: soft, value, direct
    """
    name = handle  # Use handle as name fallback
    niche_name = niche_config["name"]
    tone = niche_config["tone"]
    pain = niche_config["pain_points"][0]
    value_prop = niche_config["value_props"][0]
    opener = niche_config["dm_openers"][0].format(name=name)
    social_proof = niche_config["social_proof"]

    site_status = "has a website" if website_found else "doesn't have a website linked"
    audit_snippet = audit_summary[:300] if audit_summary else ""

    soft = f"""Write a short, casual Instagram DM from a South African web designer to @{handle}.
Context: {site_status}. Niche: {niche_name}.

Rules:
- Max 3 short paragraphs
- Very casual, no corporate language
- Compliment their page first
- Mention they might need a site, but no pressure
- Include a soft call-to-action
- Don't use emojis excessively (1-2 max)
- Sign off casually, no full name

Example tone: "hey {name}, love the vibe on your page..."
"""

    value = f"""Write a short Instagram DM offering a FREE website audit to @{handle}.
Context: {site_status}. Niche: {niche_name}.

Rules:
- Lead with value, not selling
- Mention you noticed something specific (e.g. {pain})
- Offer to send a quick audit they can read in 2 minutes
- No pricing mentioned
- Casual but competent tone
- Max 3 short paragraphs

Example angle: "happy to send over a free audit of what i'd fix..."
"""

    direct = f"""Write a direct but respectful Instagram DM to @{handle}.
Context: {site_status}. Niche: {niche_name}.

Rules:
- State the problem bluntly but kindly
- Mention the specific opportunity they're missing (e.g. {value_prop})
- Include price anchor: websites start at R2,000
- Offer examples or a quick call
- Max 3 short paragraphs
- Confident tone, not desperate

Example angle: "{name} — your page is solid but you're missing a huge piece..."
"""

    return {
        "soft": soft.strip(),
        "value": value.strip(),
        "direct": direct.strip()
    }
