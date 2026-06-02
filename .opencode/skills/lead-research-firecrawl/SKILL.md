# Lead Research — Firecrawl

## Purpose
Find leads via Firecrawl search. Discover brands that fit Outworld Creative's target markets and generate outreach angles for each.

## When to Use
- Building a new outreach target list
- Finding brands in a specific niche and location
- Researching market saturation before entering a niche
- Weekly lead discovery routine

## Inputs
- Niche (restaurant, fashion, hospitality, beauty, events, fintech)
- Location or market (Johannesburg, Cape Town, pan-Africa, global)
- Search query

## Output (JSON)
```
lead_name, url, niche, reason_fits_outworld,
visible_pain_point, outreach_angle
```

## Process
1. Run `scripts/firecrawl/research-leads.js` with niche + location
2. Review results for Outworld fit
3. Score leads by: reachability, budget potential, content gap severity
4. Select top 10 for outreach
5. Save to `memory/brands/`

## Quality Check
- [ ] Leads are in Outworld target niches
- [ ] Pain points are specific to the brand (not generic)
- [ ] Outreach angles reference actual brand observation
- [ ] No scraping of private/protected pages
- [ ] Results saved for follow-up tracking
