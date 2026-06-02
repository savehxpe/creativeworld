# Cinematic Site Remix

## Purpose
Turn an existing brand website into a premium cinematic demo landing page using Outworld's Kie API image/video pipeline. 5-step workflow with pause points at each stage for user approval.

## When to Use
- Building demo/spec landing pages for Creative Diagnosis prospects
- Creating cinematic proof-of-concept sites for client pitches
- Remixing an underperforming brand site into a premium visual experience

## Workflow

### Step 1 — Brand Analysis
**Input:** website URL, optional niche, optional notes  
**Script:** `scripts/cinematic/analyze-site.js`  
**Output:** `brand-card.html` + `brand-analysis.json` (brand name, industry, offer, audience, colors, typography clues, tone, weaknesses, trust signals, missing CTA, visual opportunities)  
**Pause point:** Ask user to approve the brand card before generating scenes.

### Step 2 — Cinematic Scene Generation
Generate 3 cinematic hero scene concepts. Each includes: scene title, emotional angle, product/service focus, camera direction, lighting, motion idea, Nano Banana 2 image prompt, Seedance 1.5 Pro video prompt.  
**Script:** `scripts/cinematic/generate-scenes.js`  
Generate 2-3 still images via Kie Nano Banana 2.  
**Kie defaults:** `model: nano-banana-2`, `aspect_ratio: 16:9`, `resolution: 1K`, `output_format: jpg`  
**Output:** `outputs/cinematic/<brand-name>/images/`  
**Pause point:** Ask user to choose the best still image before animation.

### Step 3 — Animate Selected Still
Use Kie Seedance 1.5 Pro. Create 2 animation variations.  
**Kie defaults:** `model: bytedance/seedance-1.5-pro`, `aspect_ratio: 16:9`, `resolution: 720p`, `duration: "4"`, `generate_audio: false`, `fixed_lens: false`, `nsfw_checker: false`  
**Output:** `outputs/cinematic/<brand-name>/videos/`  
**Pause point:** Ask user to choose the final video.

### Step 4 — Build Cinematic Demo Site
Build responsive single-page HTML/CSS/JS demo site.  
**Script:** `scripts/cinematic/build-demo-site.js`  
**Sections:** Hero (video background), Brand story, Product/service highlight, How it works, Proof/trust, CTA  
**Cinematic modules:** hero video background, scroll reveal, accordion cards, image trail (lightweight only), kinetic text (tasteful only), before/after comparison, hover cards  
**Performance:** hero video lightweight, poster image fallback, lazy load non-critical assets, CSS transforms only, respect `prefers-reduced-motion`, no 3D libraries, no scroll trap

### Step 5 — Deploy Prep
Do not auto-deploy unless user asks.  
Prepare: README with local preview commands, deploy instructions for Vercel, asset list, next improvement notes.

## Rules
- Never use Google APIs directly
- Never use Wavespeed
- Use `KIE_AI_API` from `.env` only
- Never print API keys
- Never commit `.env`
- Every step has a pause point for user approval
