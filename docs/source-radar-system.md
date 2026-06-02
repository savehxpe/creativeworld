# Source Radar System

Outworld Creative + saveHXPE — Internal  
Branch: creative-director

---

## Purpose

Track public sources only — RSS feeds, GitHub repos, Firecrawl results, Google Alerts exports, and saved source lists. Feed into daily authority content and stakeholder updates.

**Never** scrape private or restricted content. **Never** create claims without sources.

---

## Source Categories

| Category | Examples | Use |
|----------|----------|-----|
| AI tools | Model releases, API updates, tool launches | Signal Desk + authority scripts |
| Advertising | IAB reports, platform ad product updates | Proof content + market intel |
| Creator economy | Creator spend data, platform monetization changes | Authority content |
| Music business | IFPI reports, label deals, sync licensing | saveHXPE voice |
| Fintech | African fintech funding, product launches | Market expansion tracking |
| Fashion | Brand launches, drop culture, retail data | Spec ad relevance |
| Hospitality | Tourism data, booking trends, hotel tech | Client targeting |
| Ecommerce | SA online retail data, platform changes | Ad creative packs |
| African markets | PwC Africa outlook, DataReportal, local news | Localization + market intel |
| GitHub / open-source | Tool releases, agent frameworks | Stack awareness |
| Platform updates | Instagram, TikTok, X, LinkedIn official blogs | Content + client alerts |

---

## Source Methods

| Method | Tool | Frequency |
|--------|------|-----------|
| RSS feeds | Feed reader / `rss/` directory | Daily |
| Web search | Firecrawl `/search` | Weekly |
| Scraping | Firecrawl `/scrape` | On demand |
| Alerts | Google Alerts → email → save | Daily |
| GitHub | GH trending / saved repos | Weekly |

---

## Output Format

```
# Source Entry — [Date]

Source: [URL]
Category: [category]
Signal: [1-2 sentence summary]
Relevance to Outworld: [why it matters]
Content angle: [how to turn into a post or script]
```

Save to `sources/[category]/` or `memory/`.

---

*Internal document — not for public distribution*
