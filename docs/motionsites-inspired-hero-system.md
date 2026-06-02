# MotionSites-Inspired Hero System

Outworld Creative — Internal  
Branch: creative-director

---

## Inspiration

MotionSites builds premium animated hero prompts, templates, and animated backgrounds. The principle applied here is:

```
Minimal page. Premium animated hero. Subtle background motion. Clean agency layout. Fast load.
```

No MotionSites assets, prompts, or code were copied. Only the design principle.

---

## Current State

| Asset | Status | Path |
|-------|--------|------|
| Hero background still | Pending — Kie 401, needs key fix | `landing_page/assets/hero/outworld-cinematic-hero.jpg` |
| Fashion spec visual | Pending — Kie 401, needs key fix | `landing_page/assets/spec-work/fashion-product-drop.jpg` |
| Restaurant spec visual | Pending — Kie 401, needs key fix | `landing_page/assets/spec-work/restaurant-hospitality.jpg` |
| Fintech spec visual | Pending — Kie 401, needs key fix | `landing_page/assets/spec-work/fintech-app-sound.jpg` |

**Fallback:** CSS-only dark gradient + placeholder placeholders. Site works identically without images.

---

## Generated Asset Prompts (For When Key Is Fixed)

### 1. Hero Background (21:9)
```
Dark cinematic advertising studio atmosphere, abstract black glass environment, premium creative agency energy, subtle audio waveform geometry, soft white light trails, deep shadows, high contrast, elegant minimalism, futuristic but tasteful, no people, no logos, no text, no fake office, no clutter, no neon overload, luxury black and white palette, 21:9 cinematic composition, shallow depth, polished editorial look.
```

### 2. Fashion/Product Drop (4:5)
```
Premium fashion product drop campaign visual, dark studio lighting, luxury streetwear energy, product pedestal, black glass reflections, soft white rim light, cinematic ad composition, vertical 4:5, no text, no logos, no people, high-end agency mockup style.
```

### 3. Restaurant/Hospitality (4:5)
```
Premium restaurant and hospitality campaign visual, warm table light, dark luxury environment, cinematic food reveal energy, elegant atmosphere, shallow depth of field, black and gold warmth, no text, no logos, no people, high-end ad mockup, vertical 4:5.
```

### 4. Fintech/App (4:5)
```
Premium fintech mobile app campaign visual, abstract payment interface glow, black glass device silhouette, subtle sound wave rings, trust, speed and modern money movement, dark luxury tech aesthetic, no readable text, no logos, no people, vertical 4:5, high-end ad mockup.
```

---

## Compression Targets

| Asset | Max Size |
|-------|----------|
| Hero JPG (21:9, 1K) | < 400KB |
| Spec JPGs (4:5, 1K) | < 250KB each |

---

## Why WebM Is Postponed

- The Kie key needs re-rotation before any generation can run
- Static hero background with CSS motion (parallax, light movement, grain) already achieves the MotionSites feel
- Video adds page weight and complexity — only justified if the static version feels too still after live review

---

## Future WebM Pipeline

```
Nano Banana still (21:9)
    ↓
Seedance image-to-video (4-6 seconds)
    ↓
Export MP4/MOV
    ↓
FFmpeg compress to WebM + MP4 fallback
    ↓
Save: landing_page/assets/hero/hero-loop.webm + hero-loop.mp4
    ↓
Poster: hero-poster.jpg (first frame)
```

**WebM rules:**
- 21:9, 4-6 seconds, muted, loop, playsinline
- Poster fallback, preload="none", lazy-loaded
- Under 2-3MB
- Disabled for `prefers-reduced-motion`
- Only generated if static background feels too still after live review

---

## Reduced-Motion Rules

```css
@media (prefers-reduced-motion: reduce) {
    .hero-bg { animation: none; }
    .hero-bg-overlay { /* static */ }
    parallax: disabled;
    light-movement: disabled;
    grain: static;
    video { display: none; }
    poster { display: block; }
}
```

---

*Internal document — not for public distribution*
