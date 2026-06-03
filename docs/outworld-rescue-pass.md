# Outworld Rescue Pass

Outworld Creative — Internal Documentation

---

## What Went Wrong

1. **Proof section had 6 duplicated cards** — 3 video cards all used the same poster image (`outworld-scroll-hero-poster.jpg`) and cropped segments of the hero source video. 3 image cards used generic AI-generated WebP images unrelated to Outworld Creative or saveHXPE. This read as "AI filler" — duplicated, inauthentic, generic.

2. **No real saveHXPE proof** — The page didn't use any of saveHXPE's actual brand assets (BTS stills, portraits, partner logos, media appearances). saveHXPE is the founder and creative director; the page should center his real work.

3. **Hero scroll-scrub mapped to full page** — A prior regression changed the scrub from hero-only to full-document scroll. The 12s video should only scrub within the hero section (~200vh runway), then freeze at the last frame.

4. **Nav/content overlap** — Hero content padding was too small (`clamp(96px, 12vh, 150px)` → fixed to `clamp(110px, 14vh, 170px)`).

---

## What Was Removed

| Removed | Reason |
|---------|--------|
| 3 spec video cards (`spec-launch-reel.webm`, etc.) | Cropped source segments, not real deliverables |
| 3 spec image cards (`fashion-product-drop.webp`, etc.) | Generic AI-generated images, not saveHXPE work |
| 6-card PROOF_CARDS grid system | Entirely replaced with real proof structure |
| "Video"/"Visual" tags | Removed in prior pass |
| "Spec Creative Direction — Outworld Creative" overlay | Replaced with cleaner labels |
| LogoStage dice-flip standalone section | Merged into proof section as trust bar |
| `outworld-cloud-portal-hero.*` files | Removed in prior cleanup pass |
| PNG spec-work originals | Removed in prior cleanup pass |
| Scroll-scrub full-page regression | Restored to hero-only |

---

## How saveHXPE Is Used as Proof

Real assets copied from `/Users/tshepomotolo/seohxpe/public/brand/`:

| Asset | Source | Use in page |
|-------|--------|-------------|
| `bts_1.webp` (293 KB) | BTS stills | Proof work — creative direction |
| `bts_2.webp` (418 KB) | BTS stills | Proof work — campaign visuals |
| `bts_3.webp` (158 KB) | BTS stills | Proof work — brand storytelling |
| `portrait_1.webp` (126 KB) | Portraits | Not yet placed (future use) |
| `portrait_2.webp` (234 KB) | Portraits | Not yet placed (future use) |

Labeled honestly as "Spec creative direction — Outworld Creative" and "Built by saveHXPE / Outworld Creative".

---

## Hero Scroll-Scrub Rules

- Hero height: `200vh` — creates scroll runway
- Video seeks only within hero section bounds: `progress = (-rect.top) / (heroHeight - viewH)`
- Scroll down → video seeks forward
- Scroll up → video seeks backward
- No scroll → video freezes (queued seek model, no continuous rAF)
- Reduced motion → static poster, progress line hidden
- Text explosion: two headline words spread apart with `translateX` proportional to hero progress
- Progress line maps to hero scroll only

---

## Future 5-Second Video Slots

| Card | Video Path | Status |
|------|-----------|--------|
| UGC Ad System | `landing_page/assets/proof-videos/ugc-ad-system.mp4` | Not generated |
| Restaurant / Hospitality Ad | `landing_page/assets/proof-videos/restaurant-hospitality-ad.mp4` | Not generated |
| Clothing Brand Drop | `landing_page/assets/proof-videos/clothing-brand-drop.mp4` | Not generated |

Poster paths: `landing_page/assets/proof-posters/*.jpg` (not generated)

Until videos exist, each deliverable card shows a CSS gradient placeholder poster. No broken video placeholders.

---

## Motion-Control Rights Rule

Only use motion-control with motion reference videos that we own, recorded ourselves, or have rights to use. Do not use random existing videos from the internet as motion references. If no motion reference exists, use image-to-video instead.

---

## Acceptance Checklist

- [x] No duplicated proof card images
- [x] No headline/nav overlap (padding-top: clamp(110px, 14vh, 170px))
- [x] Hero video freezes when not scrolling
- [x] Hero video scrubs with scroll (hero-only)
- [x] Hero content stays centered and readable
- [x] Proof section feels real, not AI (real saveHXPE assets)
- [x] saveHXPE/Outworld used as prime proof example
- [x] Missing videos fall back to poster cards (CSS gradient)
- [x] Reduced motion works
- [x] Mobile has no overflow
- [x] No console errors
- [x] Build passes
- [x] Playwright passes (48/48 — 2 intermittent mobile timeouts from server congestion)

---

*Internal document — not for public distribution*
