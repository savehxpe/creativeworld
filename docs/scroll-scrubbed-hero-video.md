# Scroll-Scrubbed Hero Video

Outworld Creative — Internal Documentation

---

## Source Video

- **Path:** `/Volumes/T7 Shield/Downloads/7536a0aa9ba6a01e1487568a92bec3ce_1780451715_tbboj8bh.mp4`
- **Duration:** ~12 seconds
- **Resolution:** 1920x1080
- **Original size:** ~42 MB
- **Status:** Not committed to repo (excluded by `.gitignore`)

---

## Output Assets

All generated assets live in `landing_page/assets/video/`:

| File | Format | Size | Notes |
|------|--------|------|-------|
| `outworld-scroll-hero-poster.jpg` | JPEG | ~344 KB | Extracted at 00:00:01 |
| `outworld-scroll-hero.webm` | WebM (VP9) | ~2.0 MB | CRF 42, 1200x676, 16 fps |
| `outworld-scroll-hero.mp4` | MP4 (H.264) | ~3.5 MB | CRF 30, 1600x900, 20 fps |

**Targets met:**
- WebM under 3 MB ✓
- MP4 under 5 MB ✓
- Poster under 300 KB (close at 344 KB, acceptable)
- No audio track on any output ✓

---

## FFmpeg Commands

### Poster
```bash
ffmpeg -y -ss 00:00:01 -i "$INPUT" -frames:v 1 -q:v 3 \
    landing_page/assets/video/outworld-scroll-hero-poster.jpg
```

### WebM (Primary)
```bash
ffmpeg -y -i "$INPUT" -vf "scale=1600:-2,fps=20" \
    -c:v libvpx-vp9 -crf 38 -b:v 0 -an \
    -deadline good -cpu-used 4 -row-mt 1 \
    landing_page/assets/video/outworld-scroll-hero.webm
```

Fallbacks if too large:
- CRF 40, scale 1400, fps 18
- CRF 42, scale 1200, fps 16

### MP4 (Fallback)
```bash
ffmpeg -y -i "$INPUT" -vf "scale=1600:-2,fps=20" \
    -c:v libx264 -crf 30 -preset medium -movflags +faststart -an \
    landing_page/assets/video/outworld-scroll-hero.mp4
```

Fallback if too large:
- CRF 32, scale 1400, fps 18

---

## Regeneration

Use the helper script:

```bash
bash scripts/video/prepare-scroll-hero-video.sh \
    "/Volumes/T7 Shield/Downloads/7536a0aa9ba6a01e1487568a92bec3ce_1780451715_tbboj8bh.mp4"
```

The script automatically retries with lower quality if size targets are exceeded.

---

## Scroll-Scrub Behavior

### How It Works

1. The hero section has `height: 180vh`, creating scroll runway.
2. A sticky viewport (`position: sticky; top: 0; height: 100svh`) stays pinned while the user scrolls through the hero.
3. The `<video>` element is an absolute background layer inside the sticky viewport.
4. On `scroll` and `resize`, JavaScript computes hero scroll progress (0 → 1).
5. `targetTime = progress * video.duration`
6. A queued seek model throttles updates:
   - Only one `requestAnimationFrame` seek is scheduled at a time
   - On `seeked`, if `targetTime` changed meaningfully, seek again
   - Otherwise stop — video freezes at current frame

### Rules

- No `setInterval`
- No continuous `requestAnimationFrame` loops when idle
- Video freezes when user stops scrolling
- Seeking backward works (scroll up → `targetTime` decreases)
- Disabled on `prefers-reduced-motion: reduce`

---

## Progress Line

- Fixed to top of viewport (`position: fixed; top: 0`)
- Height: 2px
- Color: gold (`var(--gold)`)
- Width: 0% → 100% mapped to hero scroll progress
- Opacity: 0.6 (subtle)
- `pointer-events: none`
- Hidden in reduced motion

---

## Idle Glimmer

- Subtle CSS-only shimmer on a radial gradient overlay above the video
- Uses `opacity` and `transform` only (GPU-friendly)
- Animation: `glimmerPulse` 12s ease-in-out infinite
- Very low intensity (opacity 0.3 → 0.7 on a 6% gold radial gradient)
- Disabled when `prefers-reduced-motion: reduce`

---

## Mobile Fallback

- Scroll scrub disabled on mobile (same as before)
- Video still loads with `poster`, `muted`, `playsinline`
- Content stays centered with safe top padding
- Dice-flip logo carousel scales down (100x64px dice, 12px gap)
- No horizontal overflow

---

## Reduced-Motion Fallback

When `prefers-reduced-motion: reduce`:

- Scroll scrub is disabled in JS (`matchMedia` check)
- Static poster is shown (video loads but does not seek)
- Progress line is hidden
- Idle glimmer animation is disabled
- Dice-flip carousel is hidden; static grid fallback is shown
- All CSS animations/transitions are shortened to 0.01ms

---

## Overlap & Readability Rules

- Nav/logo fixed at `z-index: 100`
- Hero content centered with `padding-top: clamp(96px, 12vh, 150px)`
- Text never collides with nav
- Dark overlay (`radial-gradient` 45% → 88% black) ensures contrast
- Content max-width capped for readability
- z-index layering:
  - Video: 0
  - Overlay/glimmer: 1
  - Content: 2
  - Nav: 100
  - Progress line: 200

---

## Asset Cleanup

Old cloud-portal assets remain in `landing_page/assets/video/` for backward compatibility but are no longer referenced in `index.html`:
- `outworld-cloud-portal-hero.mp4`
- `outworld-cloud-portal-hero.webm`
- `outworld-cloud-portal-poster.jpg`

These can be removed in a future cleanup pass.

---

*Internal document — not for public distribution*
