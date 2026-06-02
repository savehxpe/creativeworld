# Cinematic Site Remix — Workflow Doc

Outworld Creative — Internal  
Branch: creative-director

---

## What It Is

The cinematic site remix pipeline takes an existing brand website and transforms it into a premium cinematic demo landing page. Uses Kie API for image generation and video animation.

---

## 5-Step Workflow

### Step 1: Analyze Brand
- Visit the brand's website
- Extract: brand name, industry, offer, audience, colors, typography clues, tone
- Identify: weaknesses, trust signals, missing CTAs, visual opportunities
- Output: `brand-card.html` (visual summary) + `brand-analysis.json` (structured data)
- **Pause:** User approves the brand card

### Step 2: Generate Scenes
- Create 3 cinematic hero scene concepts
- Each includes: scene title, emotional angle, camera direction, lighting, motion, Nano Banana prompt, Seedance prompt
- Generate 2-3 stills via Nano Banana 2
- **Pause:** User selects best still

### Step 3: Animate
- Animate selected still via Seedance 1.5 Pro
- Create 2 animation variations
- **Pause:** User selects final video

### Step 4: Build Demo Site
- Single-page HTML/CSS/JS
- Sections: Hero, Brand Story, Product, How It Works, Proof, CTA
- Hero video background with poster fallback
- Lazy-loaded, mobile-first, reduced-motion gated

### Step 5: Deploy Prep
- README + deploy instructions
- Not auto-deployed

---

## Kie Defaults

**Nano Banana 2 (stills):**
```
model: nano-banana-2
aspect_ratio: 16:9
resolution: 1K
output_format: jpg
```

**Seedance 1.5 Pro (video):**
```
model: bytedance/seedance-1.5-pro
aspect_ratio: 16:9
resolution: 720p
duration: "4"
generate_audio: false
fixed_lens: false
nsfw_checker: false
```

---

*Internal document — not for public distribution*
