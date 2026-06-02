"""
Service offerings for Outworld Creative — Creative Director Branch.
Embedded into audit logic to recommend the right service.
No prices shown publicly. Internal ranges only.
"""

SERVICES = {
    "creative_diagnosis": {
        "name": "Creative Diagnosis",
        "price_range": "R1,500 - R3,500",
        "description": "One-time strategic creative audit. Full brand analysis, 3 tailored spec ad concepts, content gap analysis, 30-day content system map, and revenue projection.",
        "includes": [
            "Brand creative audit (current state vs. potential)",
            "3 spec ad concepts tailored to your brand",
            "Content gap analysis",
            "30-day content system map",
            "Revenue projection based on creative improvements",
            "Competitor creative gap report",
            "Delivered as branded PDF within 48 hours"
        ],
        "trigger_conditions": [
            "unsure_where_to_start",
            "wants_proof_before_commitment",
            "has_budget_constraints",
            "needs_clarity_on_gaps"
        ],
        "pitch_angle": "start with clarity — understand exactly where your brand is leaking revenue and what the 200% version looks like",
        "ideal_for": "Brands that want to see the gap before investing in ongoing direction"
    },
    "monthly_direction": {
        "name": "Monthly Creative Direction",
        "price_range": "R8,000 - R20,000/month",
        "description": "Ongoing creative department for brands that need consistent premium creative without hiring full-time. Monthly campaign concepts, ad scripts, content calendars, and performance reviews.",
        "includes": [
            "8-12 short-form ad concepts per month",
            "4 polished spec/mock ad visuals",
            "4 scripts for 5-15 second videos",
            "1 monthly campaign idea with full creative direction",
            "1 offer/upsell strategy",
            "1 competitor gap report",
            "1 content calendar (30-day rollout)",
            "1 performance/next steps review",
            "Brand world system and visual rules",
            "Unlimited email/Slack access for creative direction"
        ],
        "trigger_conditions": [
            "needs_consistent_content",
            "no_in_house_creative_team",
            "wants_campaign_system",
            "ready_for_monthly_retainer"
        ],
        "pitch_angle": "get an external creative department that turns your brand into a demand-generating machine",
        "ideal_for": "Brands ready for consistent monthly creative direction and campaign execution"
    },
    "campaign_strategy": {
        "name": "Campaign Strategy",
        "price_range": "R15,000 - R40,000",
        "description": "Project-based deep-dive for launches, drops, collections, or seasonal pushes. Full campaign concept, creative direction deck, shot lists, and launch timeline.",
        "includes": [
            "Full campaign concept and big idea",
            "Creative direction deck",
            "Shot lists and moodboards",
            "Launch timeline and rollout plan",
            "Multi-platform adaptation strategy",
            "Influencer seeding strategy",
            "UGC campaign architecture",
            "Performance KPIs and measurement plan"
        ],
        "trigger_conditions": [
            "has_launch_coming",
            "needs_drop_campaign",
            "seasonal_push_needed",
            "one_time_project"
        ],
        "pitch_angle": "turn your launch into a cultural moment with campaign direction that sells out",
        "ideal_for": "Brands with specific launches, drops, or seasonal campaigns that need premium creative direction"
    },
    "brand_sound": {
        "name": "Brand Sound",
        "price_range": "Custom quote",
        "description": "Short, memorable sounds for ads, product drops, Reels, TikToks, launches and campaigns. Built to make your brand easier to remember.",
        "includes": [
            "5-second brand tags",
            "15-second ad jingles",
            "Sounds for Reels and TikTok",
            "Product reveal sounds",
            "Launch sounds",
            "Campaign music ideas"
        ],
        "trigger_conditions": [
            "no_sound_identity",
            "uses_random_trending_sounds",
            "wants_brand_recognition",
            "needs_sonic_consistency"
        ],
        "pitch_angle": "make your brand recognizable before the logo appears",
        "ideal_for": "Brands that want to own their sound, not borrow from trending audio"
    },
    "brand_world_system": {
        "name": "Brand World System",
        "price_range": "R10,000 - R25,000",
        "description": "Comprehensive brand creative identity system. Visual rules, campaign language, recurring content formats, and brand guidelines that make every piece of content feel premium and consistent.",
        "includes": [
            "Brand world creative identity",
            "Visual rules and guidelines",
            "Campaign language and tone of voice",
            "Recurring content formats",
            "Color palette and lighting direction",
            "Typography hierarchy",
            "Social post templates and safe zones",
            "Brand guideline PDF"
        ],
        "trigger_conditions": [
            "inconsistent_branding",
            "no_brand_identity",
            "content_looks_different_every_post",
            "needs_premium_positioning"
        ],
        "pitch_angle": "give your brand a creative identity so premium that people recognize your content before they see your name",
        "ideal_for": "Brands that need to elevate their entire creative presence and build consistent premium identity"
    },
    "video_ads": {
        "name": "Video Ads",
        "price_range": "Custom quote",
        "description": "Short-form video ads that hook, convert, and build brand memory. 5-second hooks, 15-second social ads, UGC-style scripts, launch videos.",
        "includes": [
            "5-second hook concepts",
            "15-second social ad scripts",
            "UGC-style scripts",
            "Campaign visuals",
            "Launch videos",
            "Product desire ads"
        ],
        "trigger_conditions": [
            "weak_hooks",
            "no_video_strategy",
            "low_conversion",
            "needs_short_form_ads"
        ],
        "pitch_angle": "turn scrolls into bookings, orders, and enquiries with video ads that stop the thumb",
        "ideal_for": "Brands that need high-converting short-form video content"
    }
}


def get_recommended_services(audit_flags, niche_key="restaurant"):
    """
    Given audit flags and niche, return recommended services.
    audit_flags: list of strings
    """
    recommendations = []
    for key, service in SERVICES.items():
        for flag in audit_flags:
            if flag in service["trigger_conditions"]:
                recommendations.append(service)
                break
    return recommendations


def get_primary_pitch(audit_flags):
    """Return the primary pitch angle for the top recommendation."""
    recommendations = get_recommended_services(audit_flags)
    if recommendations:
        return recommendations[0]["pitch_angle"]
    return "transform your brand's creative direction"


def get_service_by_key(key):
    """Get a specific service by its key."""
    return SERVICES.get(key)


def get_all_services():
    """Return all services."""
    return SERVICES
