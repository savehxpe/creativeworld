"""
AI prompts for Creative Direction Audit and Revenue Loss Analysis.
These are sent to Kimi K2/OpenCode for generating premium creative direction reports.
"""


def build_creative_audit_prompt(brand_name, niche, current_state, website_url=None, instagram_handle=None):
    """
    Build the prompt for a comprehensive creative direction audit.
    
    Args:
        brand_name: Name of the brand
        niche: restaurant, fashion, hospitality, beauty, events
        current_state: Description of current creative (from manual research)
        website_url: Optional website URL
        instagram_handle: Optional Instagram handle
    """
    digital_presence = ""
    if website_url:
        digital_presence += f"\nWebsite: {website_url}"
    if instagram_handle:
        digital_presence += f"\nInstagram: @{instagram_handle}"
    
    prompt = f"""You are a Senior Creative Director and Brand Strategist at Outworld Creative, a premium AI-powered video advertising studio for South African brands.

You have been hired to conduct a Creative Direction Audit for:

Brand: {brand_name}
Niche: {niche.replace('_', ' ').title()}{digital_presence}

Current State Summary:
{current_state}

Please provide a comprehensive but concise Creative Direction Audit with the following sections:

1. **First Impression** (2-3 sentences on brand positioning, visual identity, and immediate emotional impact)
2. **Creative Strengths** (what's working well in their current creative)
3. **Critical Gaps** (the 3 biggest creative opportunities they're missing — ranked by revenue impact)
4. **Revenue Loss Analysis** (quantify what the gaps are costing them in rands per month/year)
5. **Competitive Position** (how they compare to top competitors in their niche)
6. **The 200% Vision** (what their brand could look like with premium creative direction)
7. **Priority Fixes** (top 3 creative changes to make immediately, ranked by impact)
8. **Spec Ad Recommendations** (3 campaign concepts tailored to their brand)
9. **Content System Recommendation** (what their monthly content system should look like)
10. **Next Steps** (clear action items for the next 30, 60, 90 days)

Rules:
- Be direct but kind. This is a diagnosis, not an attack.
- Quantify revenue loss where possible (use conservative estimates).
- Reference South African market context where relevant.
- Use plain language. The reader is a business owner, not a creative director.
- Make it actionable. Every observation should lead to a clear recommendation.
- Keep the total length to 2-3 pages when formatted.
"""
    return prompt.strip()


def build_revenue_loss_prompt(niche, monthly_traffic, conversion_rate, average_order_value, current_marketing_spend=None):
    """
    Build a prompt specifically for quantifying revenue loss from creative gaps.
    """
    spend_info = f"\nCurrent Marketing Spend: R{current_marketing_spend}/month" if current_marketing_spend else ""
    
    prompt = f"""You are a Revenue Analyst at Outworld Creative, specializing in quantifying the business impact of creative gaps for South African brands.

Analyze the revenue loss for this brand:

Niche: {niche}
Monthly Digital Traffic (profile visits + website): {monthly_traffic}
Current Conversion Rate: {conversion_rate}%{spend_info}
Average Order/Booking Value: R{average_order_value}

Calculate and explain:

1. **Current Monthly Revenue** (what they're making now)
2. **Potential Monthly Revenue** (what they could make with optimized creative direction)
3. **Monthly Revenue Loss** (the gap between current and potential)
4. **Annual Revenue Loss** (multiplied by 12)
5. **Specific Creative Gaps Causing the Loss** (for this niche)
6. **ROI of Fixing the Gaps** (if creative direction investment is R10k-20k/month, what's the return?)
7. **Break-Even Timeline** (how many months to recover the investment)

Use conservative estimates. Show your math. Make it clear and compelling.

Rules:
- Be honest but not depressing. This is about opportunity, not failure.
- Show the math step by step.
- Use South African rand (R) throughout.
- Frame the creative direction investment as the smallest cost compared to the revenue gain.
"""
    return prompt.strip()


def build_200_blueprint_prompt(brand_name, niche, current_state, goals, timeline="90 days"):
    """
    Build a prompt for the 200% revenue blueprint.
    """
    prompt = f"""You are a Growth Strategist at Outworld Creative. You specialize in building 200% revenue blueprints for South African brands through creative direction.

Brand: {brand_name}
Niche: {niche}
Current State: {current_state}
Goals: {goals}
Timeline: {timeline}

Create a "200% Revenue Blueprint" — a strategic plan showing how this brand can double their revenue through creative direction.

Structure:

1. **Current State Snapshot** (where they are today)
2. **The Revenue Levers** (5 specific levers creative direction can pull)
   - For each lever:
     - What it is
     - Current performance
     - 200% performance
     - How creative direction enables it
     - Expected revenue impact
3. **The Creative Transformation** (what changes in their creative to enable 200%)
   - Visual direction changes
   - Content system changes
   - Campaign architecture changes
   - Conversion flow changes
4. **90-Day Roadmap**
   - Month 1: Foundation (what to fix first)
   - Month 2: Campaigns (what to launch)
   - Month 3: Scale (what to amplify)
5. **Investment vs. Return**
   - Estimated creative direction investment
   - Projected revenue return
   - Break-even timeline
   - 12-month projection
6. **Success Metrics** (KPIs to track)
7. **Risk Mitigation** (what could go wrong and how to prevent it)

Make it ambitious but realistic. Use South African market context. Show the math.
"""
    return prompt.strip()


def build_no_website_prompt(handle, niche, bio_text):
    """Legacy prompt — kept for compatibility with scraper system."""
    prompt = f"""You are a creative director analyzing a South African brand's Instagram presence.

Account: @{handle}
Niche: {niche.replace('_', ' ').title()}
Bio snippet: {bio_text or 'No bio available'}

This account does NOT have a website linked in their bio.

Please write a brief "Missed Opportunity Analysis" with these sections:

1. **The Problem** (why not having a digital conversion path hurts their specific niche)
2. **What They're Losing** (bookings? sales? credibility? enquiries?)
3. **What a Proper Funnel Would Fix** (3 concrete benefits tailored to this niche)
4. **Quick Win Recommendation** (suggest a simple high-converting landing page structure)

Keep it persuasive but not pushy. The tone should be expert but friendly.
"""
    return prompt.strip()
