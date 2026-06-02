# Motion Site Rules

Outworld Creative — Internal Motion Guidelines  
Branch: creative-director

---

## Philosophy

```
Motion must support trust, not distract.
Every animation needs a reason.
If motion slows the site down, remove it.
The site should feel premium, not heavy.
```

---

## Rules

### 1. Motion Serves the Offer

If an animation does not help the visitor understand what Outworld does, remove it.

**Allowed:**
- Loader that signals "something premium is loading"
- Waveform that signals "we work with sound"
- Hover effects that signal "this card is interactive"
- Reveal animations that guide the eye down the page

**Not allowed:**
- Random floating particles
- 3D worlds that delay the message
- Scroll hijacking
- Auto-playing audio

### 2. Performance First

| Metric | Target |
|--------|--------|
| Page load (mobile) | < 3 seconds |
| First Contentful Paint | < 1.5 seconds |
| Largest Contentful Paint | < 2.5 seconds |
| Cumulative Layout Shift | < 0.1 |
| Lighthouse performance | > 90 |

**How:**
- CSS animations only (no JS animation libraries)
- `transform` and `opacity` only (GPU-accelerated)
- No layout-triggering properties
- Lazy-load all video
- Compress all assets

### 3. Accessibility

```css
@media (prefers-reduced-motion: reduce) {
  * {
    animation: none !important;
    transition: none !important;
  }
  video {
    display: none;
  }
  .static-hero {
    display: block;
  }
}
```

**All motion must respect `prefers-reduced-motion`.**

### 4. Video Guidelines

- Hero video: Optional, not required. Site works without it.
- Format: `.webm` primary, `.mp4` fallback
- Size: Under 2MB
- Audio: Muted, no autoplay sound
- Poster: Static image shown before load
- Loading: `preload="none"` + `loading="lazy"`
- No video = no problem. Static gradient is the fallback.

### 5. Mobile-First

- All animations work on mobile
- Touch targets are large enough (min 44px)
- No hover-dependent interactions on mobile
- Reduced data usage: no auto-play video on mobile data

### 6. The Subtraction Rule

If the site starts to feel crowded, subtract.

If an animation feels like decoration, remove it.

If a section needs 3 animations to feel "premium," redesign the section.

---

## What to Add (Minimal)

| Element | Motion | Size |
|---------|--------|------|
| Loader | CSS fade-out | ~200 bytes |
| Hero waveform | CSS keyframes | ~300 bytes |
| Spec card hover | `transform: scale(1.02)` | ~100 bytes |
| Section reveal | `IntersectionObserver` + CSS | ~200 bytes |
| Reduced motion | `@media` query | ~100 bytes |
| **Total** | | **< 1KB** |

---

## What NOT to Add

- Three.js, WebGL, or any 3D library
- Heavy parallax scrolling
- Scroll-triggered pinning (scroll traps)
- Auto-playing audio
- Particle systems
- Glitch effects
- Neon / cyberpunk aesthetics

---

## Quality Check

- [ ] Site loads fast on 3G
- [ ] All motion respects `prefers-reduced-motion`
- [ ] No layout shift from animations
- [ ] Mobile experience is smooth
- [ ] Lighthouse score > 90
- [ ] Site feels premium without feeling heavy

---

*Internal document — not for public distribution*
