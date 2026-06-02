# Kie Workflow

Outworld Creative — Asset Production Pipeline  
Branch: creative-director

---

## Overview

The Kie workflow generates spec ad visuals for Outworld Creative. Still images are created with Nano Banana 2, then the best are animated with Seedance 1.5 Pro. Kling 3.0 is reserved for advanced motion-control needs.

---

## Production Order

```
1. Generate still with Nano Banana 2
2. Select best image
3. Animate with Seedance 1.5 Pro
4. Use Kling only when motion-reference control is needed
5. Save output URLs and asset notes
6. Compress assets before adding to the website
```

---

## Step 1: Generate Still (Nano Banana 2)

**Script:** `node scripts/kie/test-nano-banana.js`

**Prompt source:** `/docs/kie-prompts.md` — one prompt per campaign

**Process:**
1. Copy the prompt from `docs/kie-prompts.md` for the target campaign
2. Run the test script (or use the API client directly)
3. Poll task status until complete
4. Download the output image within 14 days (Kie retention policy)
5. Save to `/outputs/kie/` with campaign name

**Repeat for all 9 campaigns.** Start with #1, #4, #7 (animated priority).

---

## Step 2: Select Best Image

After generating, review each image against the spec ad concept:

- [ ] Does the image match the campaign's emotional trigger?
- [ ] Is the subject focus clear and singular?
- [ ] Is the lighting premium and intentional?
- [ ] Is there sufficient negative space for the headline?
- [ ] Does it feel like a campaign still from a serious agency?

Select the best variant. If none pass, re-generate with adjusted prompt.

---

## Step 3: Animate (Seedance 1.5 Pro)

**Script:** `node scripts/kie/test-seedance.js [image_url]`

**Only animate 3 ads:** #1 (Restaurant), #4 (Fashion), #7 (Hospitality)

**Process:**
1. Pass the selected Nano Banana output URL as `image_url`
2. Use the campaign's video prompt from `docs/kie-prompts.md`
3. Default: 4 seconds, 9:16, no audio
4. Poll task status until complete
5. Download the output video
6. Create a poster frame (first frame or key moment)

---

## Step 4: Motion Control (Kling 3.0 — Future)

**Only when Seedance motion needs refinement.** Requires:
- A Nano Banana still (image URL)
- A reference motion video (video URL)

Skip this step until you have both inputs ready.

---

## Step 5: Save + Track

**Asset Manifest:** Create `/outputs/kie/asset-manifest.json`:

```json
{
  "campaigns": [
    {
      "id": 1,
      "name": "The Reservation You Can't Get",
      "niche": "restaurant",
      "animated": true,
      "still": {
        "taskId": "...",
        "outputUrl": "...",
        "localPath": "outputs/kie/campaign-1-restaurant.jpg",
        "generatedAt": "2025-01-01T00:00:00Z"
      },
      "video": {
        "taskId": "...",
        "outputUrl": "...",
        "localPath": "outputs/kie/campaign-1-restaurant.mp4",
        "posterPath": "outputs/kie/campaign-1-restaurant-poster.jpg",
        "generatedAt": "2025-01-01T00:00:00Z"
      }
    }
  ]
}
```

**Download all assets within 14 days** — Kie deletes files after this period.

---

## Step 6: Compress + Deploy

**Before adding to website:**
1. Convert images to WebP (smaller than JPG)
2. Resize to 1080px max width
3. Compress videos to under 2MB
4. Create poster frames for all videos
5. Add `loading="lazy"` and `preload="none"` attributes

**Update landing page:**
1. Replace spec card placeholder divs with `<img>` tags
2. Add video elements for animated ads
3. Set poster attributes
4. Test locally: `python3 -m http.server 8000`
5. Deploy to GitHub Pages

---

## Budget Tracking

| Model | Cost/Unit | 9 Units | Budget |
|-------|-----------|---------|--------|
| Nano Banana 2 (1K) | $0.04 | $0.36 | Under $5 |
| Seedance 1.5 Pro (4s) | ~$0.06/s | ~$0.72 (3 ads) | Under $5 |
| **Total (9 stills + 3 animated)** | | **~$1.08** | **Budget: $5** |

---

*Internal document — not for public distribution*
