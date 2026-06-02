# Asset Optimizer

## Purpose
Prepare generated images and videos for the Outworld Creative website. Compress, create poster frames, enable lazy loading, and follow mobile-first performance rules.

## When to Use
- After Kie.ai generates spec ad images (before adding to landing page)
- After Seedance generates video (before embedding)
- Before deploying any visual update to the website
- When adding new spec ad cards with real visuals

## Process

### For Images
1. **Download** from Kie.ai output URL within 14 days
2. **Save locally** to `/assets/spec-lab/` with consistent naming:
   - `campaign-1-restaurant-reservation.webp`
3. **Convert to WebP** if not already — better compression
4. **Resize** to max 1080px width (4:5 = 1080x1350)
5. **Update** the `<img src="...">` in `landing_page/index.html`

### For Videos
1. **Download** from Kie.ai output URL
2. **Create poster frame** (first frame or key moment)
3. **Compress** video: target < 2MB, use `.webm` + `.mp4` fallback
4. **Add attributes:** `preload="none" loading="lazy" poster="poster.jpg"`
5. **Update** the spec card video element

### Post-Processing Checklist
- [ ] Files are named consistently
- [ ] Images are WebP format, compressed
- [ ] Videos are under 2MB with poster frames
- [ ] `loading="lazy"` on all images and videos
- [ ] `prefers-reduced-motion` fallback considered
- [ ] Page load time tested after adding assets

## Naming Convention
```
/outworld/assets/spec-lab/
  campaign-[number]-[niche]-[short-name].[ext]

Example:
  campaign-1-restaurant-reservation.webp
  campaign-1-restaurant-reservation.mp4
  campaign-1-restaurant-reservation-poster.jpg
```

## Quality Check
- [ ] Lighthouse performance score > 90 after adding assets
- [ ] Images are appropriately sized (not full-resolution 4K for a 350px card)
- [ ] Videos lazy-load and don't autoplay
- [ ] Poster frames provide context before video loads
- [ ] File sizes are tracked in asset manifest
