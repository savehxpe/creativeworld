# MotionSites-Inspired Subtraction Pass

Outworld Creative — Internal  
Branch: creative-director

---

## What Changed

The landing page was reduced from 6 sections to 4 sections, inspired by the MotionSites principle of premium minimalism: one strong moving background, simple centered copy, glass UI, minimal navigation.

---

## What Was Removed

| Removed | Why |
|---------|-----|
| **Signal Desk section** (paragraph + 9 tag pills) | Internal content system. Not a public product. Signal Desk is valuable as a backend tool — it should live on a separate page or be private. |
| **Selected Spec Work** (3 featured + 6 collapsed cards) | Portfolio wall. Premature for a home page. Spec work lives in the backend and can be a separate product page later. |
| **Duplicate hero logo** | Overkill. Only one logo mark needed — in the nav. |
| **Loader with logo** | Removed entirely. Page loads fast enough without a loader. |
| **Waveform animation** | Replaced by the cinematic African-global background image. |
| **"Built from Africa" tagline** | Moved to footer — not a hero-level element. |
| **Founder line in hero** | Moved to footer. |
| **Pull quote** ("Most brands have a look...") | Removed. Concept is embedded in the Brand Sound capability card. |
| **Brand Sound standalone section** | Already removed in prior pass — merged into capability card. |
| **Long service descriptions** | Already removed in prior pass — cards are 1-2 sentences each. |

## What Was Kept

| Kept | Why |
|------|-----|
| **Hero** — centered, full viewport, single H1 + 2-line copy + glass CTA button | The one thing people see first |
| **Proof Logos** — 15-brand carousel with actual .webp assets from saveHXPE | Trust signals. Real partners, not claims. |
| **What We Do** — 3 capability cards (Short-form Ads, Brand Sound, Campaign Direction) | The offer. Clear. Simple. |
| **CTA** — email + founder footer | The next step |

---

## Background Motion System

The hero uses a Kie-generated African-global cinematic image (`outworld-african-global-hero.png`, 1665KB) with:

- **Dark overlay** — gradient from 50% to 90% opacity, keeping text readable
- **Grain overlay** — 3% opacity SVG noise texture for cinematic feel
- **Light movement** — 20s CSS keyframe oscillation filtering brightness 1.0→1.1 + subtle scale
- **No parallax** yet — kept simple. Parallax can be added if motion feels too static.

**Reduced-motion fallback:** All animations disabled. Static background only.

---

## Logo Scroll Rotation

Single logo in the fixed nav rotates subtly (0°→20°) based on scroll progress:

```javascript
// use requestAnimationFrame for smooth, throttled rotation
const pct = scrollY / (scrollHeight - viewportHeight);
const rotation = Math.min(pct * 20, 20);
logo.style.transform = `rotateY(${rotation}deg)`;
```

**Effect:** As the user scrolls, the logo gently rotates like a 3D mark revealing depth. Stops at 20° max.

**Reduced-motion:** Transform set to `none` via CSS media query.

---

## Brand Logos

Logos were copied from `/Users/tshepomotolo/seohxpe/public/brand/partners/` and `appearances/` to `landing_page/assets/brand/`. All are local `.webp` files — no hotlinking. Vercel can serve them.

**Label:** "Trusted across music, culture and media." Not "clients." Not "partners." Generic trust signal.

---

## Future WebM Rules

Only add a 4-6 second WebM hero loop if the static feel is too still after live review:

- 21:9 or 16:9, muted, loop, playsinline
- Poster fallback from current static hero PNG
- `preload="none"`, lazy-loaded
- Under 2-3MB, MP4 fallback
- Disabled for reduced motion

---

## Page Stats

| Metric | Before | After |
|--------|--------|-------|
| Sections | 6 | 4 |
| Lines of HTML | 467 | 260 |
| Loader | Yes (logo + fade) | No |
| Kie images on page | 4 (hero + 3 spec) | 1 (hero only) |
| Cards | 6 (3 featured + 3 capability + 6 collapsed) | 3 |
| Nav links | 4 | 2 |
| Playwright tests | 13 × 3 + 9 visual = 48 | 9 × 3 + 9 visual = 36 |

---

*Internal document — not for public distribution*
