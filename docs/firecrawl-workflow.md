# Firecrawl Workflow

Outworld Creative — Internal  
Branch: creative-director

---

## Overview

Firecrawl provides research and extraction power. Combined with Outworld's creative engines, it automates lead research, brand audits, competitor scans, and Creative Diagnosis preparation.

---

## 3 Pipelines

### 1. Brand Audit (`audit-brand.js`)

**Input:** Brand website URL + optional niche  
**Output JSON:** brand summary, offer, audience, current CTA, trust signals, content gaps, ad opportunities, brand sound opportunity, 3 Creative Diagnosis bullets, 3 outreach angles

**Use:** Pre-call research for discovery calls. Feeds into Creative Diagnosis reports.

### 2. Competitor Scan (`competitor-scan.js`)

**Input:** Brand URL + 1-3 competitor URLs  
**Output JSON:** competitor positioning, visual gaps, offer gaps, CTA gaps, proof gaps, content angles, 5 ad ideas

**Use:** Building competitor gap reports. Informing spec ad concepts.

### 3. Lead Research (`research-leads.js`)

**Input:** Niche + location + search query  
**Output JSON:** lead name, URL, niche, reason fits Outworld, visible pain point, outreach angle

**Use:** Building target lists for outreach. Finding brands to send spec ad previews to.

---

## Usage

```bash
# Brand audit
node scripts/firecrawl/audit-brand.js https://example.com restaurant

# Competitor scan
node scripts/firecrawl/competitor-scan.js https://brand.com https://competitor1.com https://competitor2.com

# Lead research
node scripts/firecrawl/research-leads.js "restaurant" "Johannesburg" "best restaurants joburg instagram"
```

---

## Security

- `FIRECRAWL_API_KEY` read from `.env` (not committed)
- Never logged or printed
- No paid API calls auto-executed without user confirmation

---

*Internal document — not for public distribution*
