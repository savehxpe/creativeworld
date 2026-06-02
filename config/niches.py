"""
Niche configuration for Outworld Lead Engine.
Each niche has specific tone, examples, and pain points.
"""

NICHES = {
    "musician": {
        "name": "Musician / Artist",
        "tone": "creative peer",
        "examples": [
            "booking inquiries",
            "press kit",
            "fan mailing list",
            "streaming links",
            "gig calendar"
        ],
        "pain_points": [
            "promoters can't find their portfolio quickly",
            "fans have nowhere to buy merch or tickets",
            "no central place for all streaming links",
            "looks amateur when industry contacts search them"
        ],
        "dm_openers": [
            "hey {name}, love the sound 🔥",
            "{name}, your latest drop is hard 👏",
            "been following your page — the vibe is solid"
        ],
        "value_props": [
            "a site that actually gets you booked",
            "one link that has everything — Spotify, Apple Music, YouTube, tickets",
            "look professional when labels or promoters Google you",
            "stop losing fans to broken Linktree pages"
        ],
        "social_proof": "i've built sites for artists in SA and they get more booking DMs within a week"
    },
    "clothing_brand": {
        "name": "Clothing Brand",
        "tone": "business-aware",
        "examples": [
            "lookbook",
            "checkout flow",
            "size guide",
            "brand story",
            "stockist list"
        ],
        "pain_points": [
            "customers can't buy directly — must DM to order",
            "no size guide = more returns and complaints",
            "brand looks like a hobby, not a business",
            "losing sales to competitors with proper sites"
        ],
        "dm_openers": [
            "hey {name}, the new drop looks clean 👕",
            "{name}, been eyeing the latest collection",
            "your brand aesthetic is strong — just noticed something"
        ],
        "value_props": [
            "a site where customers can buy without DMing you",
            "lookbook pages that actually sell",
            "look like the established brands you compete with",
            "stop losing sales because people can't find your shop"
        ],
        "social_proof": "i help SA clothing brands turn their Instagram hype into actual website sales"
    }
}


def detect_niche(handle, bio_text, website_content):
    """
    Simple heuristic niche detection.
    Returns 'musician' or 'clothing_brand'.
    """
    text = f"{bio_text} {website_content}".lower()

    music_keywords = [
        "music", "artist", "rapper", "producer", "dj", "band", "hip hop",
        "rap", "amapiano", "gospel", "r&b", "singer", "songwriter",
        "mixtape", "album", "single", "studio", "beats", "vocals"
    ]

    clothing_keywords = [
        "fashion", "clothing", "apparel", "streetwear", "boutique",
        "label", "brand", "wear", "threads", "garments", "collection",
        "drop", "lookbook", "designer", "outfit", "style"
    ]

    music_score = sum(1 for kw in music_keywords if kw in text)
    clothing_score = sum(1 for kw in clothing_keywords if kw in text)

    return "clothing_brand" if clothing_score > music_score else "musician"


def get_niche_config(niche_key):
    return NICHES.get(niche_key, NICHES["musician"])
