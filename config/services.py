"""
Service offerings for Outworld Lead Engine.
Embedded into audit logic to recommend the right service.
"""

SERVICES = {
    "website": {
        "name": "Website Design",
        "price": "R2,000",
        "description": "3-5 page mobile-responsive website (Home, About, Gallery/Work, Contact)",
        "includes": [
            "Mobile-responsive design",
            "Basic SEO setup",
            "Contact form integration",
            "Social media links",
            "2 rounds of revisions"
        ],
        "trigger_conditions": [
            "no_website",
            "broken_website",
            "poor_mobile_experience",
            "slow_performance",
            "outdated_design"
        ],
        "pitch_angle": "get you a proper online home that converts visitors into fans/customers"
    },
    "branding": {
        "name": "Branding & Graphics",
        "price": "Custom quote",
        "description": "Logo refinement, colour palette, typography, brand guidelines",
        "includes": [
            "Logo concepts",
            "Colour palette",
            "Typography system",
            "Social media templates",
            "Brand guideline PDF"
        ],
        "trigger_conditions": [
            "inconsistent_branding",
            "no_logo",
            "poor_visual_identity"
        ],
        "pitch_angle": "make your brand look as professional as your talent"
    },
    "seo": {
        "name": "SEO Audit & Fix",
        "price": "R500 – R800",
        "description": "Technical SEO audit + on-page fixes",
        "includes": [
            "Lighthouse SEO score improvement",
            "Meta tags & headings fix",
            "Image optimization",
            "Mobile usability fixes",
            "Sitemap submission"
        ],
        "trigger_conditions": [
            "low_seo_score",
            "missing_meta_tags",
            "poor_mobile_seo"
        ],
        "pitch_angle": "make sure Google actually finds you when people search"
    }
}


def get_recommended_services(audit_flags):
    """
    Given a list of audit flags, return recommended services.
    audit_flags: list of strings like 'no_website', 'low_seo_score'
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
    return "level up your online presence"
