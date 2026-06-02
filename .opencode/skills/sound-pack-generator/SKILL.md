# Sound Pack Generator

## Purpose
Generate a 3-part Brand Sound Pack for Outworld Creative clients:

1. 3-second brand tag
2. 15-second Reel/TikTok loop
3. 10-second podcast or ad intro/outro

## When to Use
- Building a new brand sound identity for a client
- Creating proof assets for the Spec Ad Lab
- Responding to a Creative Diagnosis with sound concepts
- Selling the Brand Sound Pack as a standalone product

## Process

### Step 1: Define the Brand
- Niche: restaurant, fashion, hospitality, beauty, events, fintech, podcast
- Mood: warm, confident, calm, clean, FOMO, modern, sharp
- Tempo: niche-appropriate BPM

### Step 2: Generate 3 Variations
For each sound in the pack, use the sounds endpoint with slight prompt variations:

**3-Second Brand Tag:**
```
Create a 3-second brand tag for a [NICHE] brand.
Mood: [MOOD]. Tempo: [BPM].
Style: short, memorable, clean, modern brand cue.
No vocals. No melody development. Just a signature sound.
```

**15-Second Social Loop:**
```
Create a 15-second loopable brand sound for [NICHE] Reels and TikTok.
Mood: [MOOD]. Tempo: [BPM].
Style: premium, clean, minimal, modern.
Should loop seamlessly for social media ads.
```

**10-Second Intro:**
```
Create a 10-second brand intro for [NICHE] ads and content.
Mood: [MOOD]. Tempo: [BPM].
Style: premium, clean build-up, modern.
Short enough for ad intros, long enough to establish the brand.
```

### Step 3: Select + Export
- Review all 3 variations
- Select the best for each use case
- Export as WAV (uncompressed) + MP3 (compressed)
- Name: `[brand]_[type]_[BPM].wav`

### Step 4: Pair with Visual
- Match the sound pack with a Kie-generated still or video
- Create a combined spec ad preview (visual + sound)

### Step 5: Rights Check
- Run audio-rights-check before any commercial delivery
- Record prompt, date, model, account tier, task ID

## Output Package
```
Brand Sound Pack: [Brand Name]

1. Brand Tag (3s)
   File: brand_tag_3s.wav
   Use: Social ads, Reels opening, profile sound

2. Social Loop (15s)
   File: social_loop_15s.wav
   Use: Reels/TikTok ads, campaign background

3. Intro/Outro (10s)
   File: intro_10s.wav
   Use: Podcast, long-form content, brand films

Usage License: Included
Rights: Confirmed via audio-rights-check
Producer: Outworld Creative
```

## Quality Check
- [ ] All 3 sounds share a consistent sonic identity
- [ ] Tag is recognizable in 1-2 seconds
- [ ] Loop transitions seamlessly
- [ ] Intro has a clear start and end
- [ ] No artist names in prompts
- [ ] Commercial rights confirmed
