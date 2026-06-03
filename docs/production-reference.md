# Production Reference

Outworld Creative — Locked Production Snapshot

---

## Reference Deployment

- **URL:** `https://outworld-k235nzzru-cisse-creates-projects.vercel.app/`
- **Aliased:** `https://outworld.vercel.app`
- **Date:** 2026-06-03
- **Commit:** `ba77a86`
- **Commit message:** Fix dice-flip, full-page scroll, nav glass, spec work images + videos
- **Branch:** `creative-director` (at time of deploy)

---

## What This Production Version Represents

This is the stable production reference before the rescue pass. It includes:

- Scroll-scrubbed hero video (WebM only, 2MB) mapped to full-page scroll
- Dice-flip logo carousel (200px desktop dice)
- Nav glass banner with backdrop blur
- Proof section with 3 spec video cards + 3 spec image cards
- "Ideas that stick." tagline
- All 48 Playwright tests passing

---

## Separation Rule

Future experimental changes (rescue pass, proof system redesign, etc.) must happen on separate branches:

- `rescue-proof-system` — active experiment branch
- `creative-director` — working/development branch
- `production-reference` — locked backup of this production state

**Do not push untested rescue changes to production without promoting a verified deployment.**

---

## Rollback Procedure

If the rescue deployment causes issues:

```bash
vercel promote https://outworld-k235nzzru-cisse-creates-projects.vercel.app/ --yes
```

Or via Vercel Dashboard → Deployments → `outworld-k235nzzru` → Promote to Production.

---

*Internal document — not for public distribution*
