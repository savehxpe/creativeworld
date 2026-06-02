# Suno Brand Sound Workflow

Outworld Creative — Internal  
Branch: creative-director

---

## Overview

Suno generates brand sounds — 3-second tags, 15-second loops, campaign audio cues. Paired with Kie visuals, this creates complete ad assets that brands can see, hear, and remember.

---

## Production Order

```
1. Pick niche + define brand emotion
2. Generate 3 sound directions
3. Select best one
4. Export short versions
5. Pair sound with Kie-generated visual/video
6. Save records: prompt, date, model, account tier, usage note
7. Do NOT sell unless commercial rights are confirmed
```

---

## Step 1: Define Brand Emotion

Before generating, define:
- **Niche:** restaurant, fashion, hospitality, beauty, events, fintech, podcast
- **Mood:** warm, confident, calm, clean, FOMO, modern, sharp
- **Use case:** 3-second tag, 15-second Reel/TikTok loop, 10-second intro
- **Tempo:** niche-appropriate BPM (see API docs)

---

## Step 2: Generate 3 Sound Directions

Use the sounds endpoint (`/api/v1/generate/sounds`):

```bash
node scripts/suno/test-sound.js
```

**Prompt format:**
```
Create a short loopable brand sound for a [NICHE] campaign.

Mood: [MOOD]
Use case: [use case]
Tempo: [BPM]
Style: modern, clean, memorable, minimal, premium
Avoid: vocals, copyrighted melodies, artist imitation, busy drums, long build-ups

The sound should feel like a brand cue people can remember after hearing it once.
```

Generate 3 variants per sound pack with slight prompt variations.

---

## Step 3: Select Best One

Review each generated sound:
- [ ] Is it recognizable in 1-2 seconds?
- [ ] Does it match the brand emotion?
- [ ] Is it free from obvious reference imitation?
- [ ] Does it loop cleanly (no jarring transitions)?
- [ ] Would a brand pay for it?

---

## Step 4: Export Short Versions

From the selected sound:
1. Trim to 3-second tag
2. Trim to 15-second loop
3. Trim to 10-second intro/outro
4. Export as WAV + MP3
5. Name: `[brand]_[niche]_[type]_[version].wav`

---

## Step 5: Pair with Kie Visual

Combine with the corresponding Kie-generated still or video:
- Restaurant sound + "The Reservation You Can't Get" still
- Fashion sound + "The Drop That Sold Out in 4 Hours" video
- Hospitality sound + "Wake Up Here" video

---

## Step 6: Save Records

For every generated sound, record:
- Prompt text
- Generation date
- Model version (V5)
- Account tier (Pro/Premier — must be commercial eligible)
- Task ID
- Output file paths
- Usage note (commercial / non-commercial)

Store in `memory/sounds/` for audit trail.

---

## Step 7: Rights Check

Before delivering to any client, run the `audio-rights-check` skill:
- [ ] Generated under commercial-use eligible account?
- [ ] Generated after paid/commercial plan became active?
- [ ] Prompt, date, model, task ID recorded?
- [ ] Free from copied lyrics, artist names, imitation prompts?
- [ ] Client receiving a usage license?
- [ ] Producer has edited/finished the output?

**If any fail → do not sell.**

---

## Budget Tracking

| Niche | Sound Pack Name | Suno Credits Used | Status |
|-------|----------------|-------------------|--------|
| Restaurant | Table Booked | — | Pending |
| Fashion | Drop Alert | — | Pending |
| Hospitality | Wake Up Here | — | Pending |
| Beauty | Soft Trust | — | Pending |
| Events | You Had To Be There | — | Pending |
| Fintech | Money Moves Clean | — | Pending |
| Podcast | Signal Intro | — | Pending |

---

*Internal document — not for public distribution*
