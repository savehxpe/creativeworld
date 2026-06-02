# Motion Site Engine

Outworld Creative — Internal Skill  
Branch: creative-director

---

## Purpose

Define the motion and animation rules for the Outworld Creative website. Keep it premium, light, and accessible.

---

## Motion Philosophy

```
Motion must support trust, not distract.
If an animation does not help the visitor understand the offer, remove it.
If motion slows the site down, remove it.
If the site starts to feel crowded, subtract.
```

---

## Allowed Motion

| Element | Motion | Implementation |
|---------|--------|---------------|
| **Loader** | Fade-in overlay, 1s dissolve | CSS keyframes, no JS |
| **Hero** | Optional silent looping video | `<video>` with poster, lazy-loaded |
| **Logo carousel** | CSS marquee, auto-scroll | `transform: translateX`, infinite loop |
| **Spec Ad cards** | Hover scale + subtle glow | `transform: scale(1.02)`, box-shadow |
| **Section reveals** | Fade-up on scroll | `IntersectionObserver` + CSS |
| **Waveform** | CSS bar animation | Keyframes, no JS |

---

## Performance Rules

- **Hero video:** Under 2MB. `.webm` primary, `.mp4` fallback.
- **Lazy loading:** `preload="none"` + `loading="lazy"` on all video
- **Poster images:** Static frame shown before video loads
- **CSS only:** No layout-triggering properties (no `width`, `height`, `margin` animations)
- **`transform` and `opacity` only:** GPU-accelerated, no reflow
- **No heavy 3D:** No Three.js, no WebGL, no 1MB+ libraries
- **No scroll traps:** User can scroll freely, no forced scroll-hijacking

---

## Accessibility

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

**All motion respects `prefers-reduced-motion`.**

---

## Quality Check

- [ ] Page loads in under 3 seconds on mobile
- [ ] Lighthouse performance score > 90
- [ ] All motion works without JS (progressive enhancement)
- [ ] Reduced motion fallback works
- [ ] No motion causes layout shift (CLS < 0.1)

---

## Example Use

**Hero loader:**
```css
.loader {
  position: fixed;
  inset: 0;
  background: #0a0a0a;
  z-index: 9999;
  animation: fadeOut 1s ease 0.5s forwards;
}
@keyframes fadeOut {
  to { opacity: 0; pointer-events: none; }
}
```

**Hero video (optional):**
```html
<video autoplay muted loop playsinline
       preload="none"
       poster="hero-poster.jpg"
       loading="lazy">
  <source src="hero.webm" type="video/webm">
  <source src="hero.mp4" type="video/mp4">
</video>
```

---

*Internal skill — not exposed on public website*
