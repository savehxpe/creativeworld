# Liquid-Glass Upgrade

Outworld Creative — Internal  
Branch: creative-director

---

## What Changed

The Outworld landing page was upgraded from vanilla HTML/CSS to a **React 18 + Tailwind + Framer Motion** single-file app with a **liquid-glass design system** inspired by the MotionSites cinematic direction.

---

## Tech Stack

| Layer | Implementation |
|-------|---------------|
| **Rendering** | React 18 via CDN (`react@18.3.1`, `react-dom@18.3.1`) |
| **Compilation** | Babel standalone in-browser (`@babel/standalone@7.29.0`) |
| **Styling** | Tailwind CDN + custom `.liquid-glass` / `.liquid-glass-strong` CSS |
| **Animation** | Framer Motion 11.11.17 via CDN |
| **Font** | DM Sans variable weight (Google Fonts) |
| **Video** | Custom `FadingVideo` component with rAF-driven crossfade |

---

## Liquid-Glass CSS System

Two variants, both using `backdrop-filter: blur()` + `::before` gradient border via mask compositing.

### `.liquid-glass` — Subtle (nav, cards)
- `backdrop-filter: blur(4px)`
- `rgba(255,255,255,0.01)` background
- Inset box-shadow: `0 1px 1px rgba(255,255,255,0.1)`
- `::before` gradient border: 0.45 → 0.15 → 0 → 0 → 0.15 → 0.45

### `.liquid-glass-strong` — Heavy (primary CTA)
- `backdrop-filter: blur(50px)`
- Same background + mask-composite technique
- Drop shadow: `4px 4px 4px rgba(0,0,0,0.05)`
- `::before` gradient border: 0.5 → 0.2 → 0 → 0 → 0.2 → 0.5

---

## Components

| Component | Purpose |
|-----------|---------|
| **FadingVideo** | rAF-driven opacity crossfade. Supports both `<video>` (loop via `ended` event) and `<img>` (static PNG fallback). `loadeddata → fadeTo(1)`. Fade-out lead: 0.55s before video ends. Cleanup on unmount cancels rAF. |
| **BlurText** | `IntersectionObserver`-triggered word-by-word blur-in. Each word is a `motion.span` with 3-step keyframes: `blur:10→5→0`, `opacity:0→0.5→1`, `y:50→-5→0`. Stagger: `i × 100ms`. Applied to hero subtitle (11 words). |
| **Navbar** | Fixed top, 1 logo (PNG), liquid-glass pill wrapping "What We Do" + "Contact" links |
| **Hero** | Full viewport, FadingVideo BG (PNG African-global image), dark overlay, grain texture, BlurText subtitle, liquid-glass-strong CTA |
| **Logos** | CSS marquee — 15 brand logos with gradient fade edges. Non-React (vanilla HTML + CSS) for zero animation overhead |
| **WhatWeDo** | 3 liquid-glass cards. Framer Motion `containerVariants` + `cardVariants` with `staggerChildren: 0.2`. Triggered by `whileInView`. |
| **CTA** | Liquid-glass-strong email link |
| **Footer** | Simple, static |

---

## Framer Motion Animation Timeline

| Element | Trigger | Animation |
|---------|---------|-----------|
| H1 "Outworld Creative" | Page load + 0.2s | blur:10→0, opacity:0→1, y:20→0 |
| BlurText (11 words) | IntersectionObserver on hero | Word-by-word blur-in, 100ms stagger |
| Hero body copy | Page load + 1.2s | blur + fade + y slide |
| Hero CTA button | Page load + 1.5s | blur + fade + y slide |
| What We Do cards | `whileInView` | stagger: 0.2s per card, blur+fade+y slide |

---

## Performance

| Metric | Before | After |
|--------|--------|-------|
| HTML size | 260 lines | ~340 lines |
| External scripts | 0 | 5 CDN (~150KB gzipped) |
| TTFS | ~50ms | ~300ms (Babel parse + React mount) |
| Page weight | ~1.7MB (hero PNG) | ~1.85MB |
| Reduced-motion | CSS `animation-duration: 0.01ms` | CSS override still works (Framer Motion respects `prefers-reduced-motion` natively) |

---

## Reduced-Motion

```css
@media (prefers-reduced-motion: reduce) {
    *, *::before, *::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
    .logo-marquee { animation: none; }
}
```

Framer Motion also respects the OS-level reduced-motion setting and skips animations automatically.

---

*Internal document — not for public distribution*
