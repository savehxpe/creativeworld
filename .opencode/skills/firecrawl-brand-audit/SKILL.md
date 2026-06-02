# Firecrawl Brand Audit

## Purpose
Run a complete brand audit via Firecrawl scraping. Extract brand positioning, offer, audience, CTA quality, trust signals, content gaps, ad opportunities, and brand sound gaps. Feed directly into Creative Diagnosis reports.

## When to Use
- Before a discovery call (pre-call research)
- Building a Creative Diagnosis for a prospect
- Auditing a competitor's digital presence
- Generating outreach angles for cold contacts

## Inputs
- Brand website URL (required)
- Optional: Instagram URL
- Optional: Niche

## Output (JSON)
```
brand_summary, niche, offer, audience, current_cta,
trust_signals, content_gaps, ad_opportunities,
brand_sound_opportunity, 3 diagnosis_bullets, 3 outreach_angles
```

## Process
1. Scrape brand website via `lib/firecrawl/client.js`
2. Extract structured data from page content
3. Map to Creative Diagnosis framework
4. Generate diagnosis bullets and outreach angles
5. Save results to `memory/brands/`

## Quality Check
- [ ] All fields populated (no "pending" without good reason)
- [ ] Diagnosis bullets are specific to the brand
- [ ] Outreach angles are actionable, not generic
- [ ] Brand sound opportunity is noted
- [ ] No fabricated data or unsourced claims
