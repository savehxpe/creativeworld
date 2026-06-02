# Research to Diagnosis Pipeline

Outworld Creative — Internal  
Branch: creative-director

---

## Purpose

How Firecrawl research feeds into Creative Diagnosis reports — the end-to-end pipeline from scraping to client-ready deliverable.

---

## Pipeline

```
1. SCRAPE
   Firecrawl scrapes brand website + competitor sites
   Output: raw markdown content

2. ANALYZE
   Scripts extract structured data:
   - brand summary
   - offer and audience
   - CTA quality
   - trust signals
   - content gaps
   Output: JSON analysis

3. DIAGNOSE
   Creative director agent generates:
   - Creative audit
   - Revenue loss analysis
   - 200% blueprint
   - 3 spec ad concepts
   Output: diagnosis draft

4. VALIDATE
   Run evals against diagnosis:
   - spec-ad-lab eval
   - brand-sound eval
   Output: approved or flagged

5. DELIVER
   Package as Creative Diagnosis Report (PDF)
   Include: audit, revenue loss, blueprint, spec ads
   Output: client-ready deliverable

6. SAVE
   Store everything in memory:
   - memory/brands/ (brand profile)
   - memory/campaigns/ (diagnosis outcomes)
   - memory/hooks/ (winning hooks from spec ads)
```

---

## Example Flow

```bash
# 1. Scrape brand
node scripts/firecrawl/audit-brand.js https://example-restaurant.com restaurant

# 2. Scrape competitors
node scripts/firecrawl/competitor-scan.js https://example.com https://comp1.com https://comp2.com

# 3. Feed results into creative director (manual or automated)
# 4. Generate Creative Diagnosis PDF
# 5. Save to memory
```

---

## Integration Points

| Firecrawl Output | Feeds Into |
|-----------------|-----------|
| brand_audit.json | Creative Diagnosis → revenue-leak-engine |
| competitor_scan.json | Creative Diagnosis → spec-ad-engine |
| lead_research.json | Outreach → outreach-engine |

---

*Internal document — not for public distribution*
