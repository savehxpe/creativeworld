# Generate Sounds — Model Reference

Suno API Internal Documentation  
Branch: creative-director

---

## Overview

The Generate Sounds endpoint is designed for loops, BPM, key, and ambient/background use cases. This is the primary endpoint for Outworld brand sound — 3-second tags, 15-second social loops, product reveal sounds, and podcast intros.

**Use for:** Brand sound packs, Reels/TikTok loops, product reveal sounds, campaign audio cues.

---

## API

### Endpoint
```
POST https://api.sunoapi.org/api/v1/generate/sounds
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `prompt` | string | — | Text prompt describing the sound |
| `model` | string | `V5` | Model version |
| `soundLoop` | boolean | `true` | Create loopable output |
| `soundTempo` | number | — | BPM (recommend 85-130 depending on niche) |
| `soundKey` | string | `Any` | Musical key |
| `grabLyrics` | boolean | `false` | Extract lyrics (not relevant for brand sound) |

### Response

```json
{
  "taskId": "...",
  "status": "processing"
}
```

---

## Outworld Defaults

```
model: V5
soundLoop: true
soundTempo: niche-dependent (see below)
soundKey: Any
grabLyrics: false
```

---

## Per-Niche Sound Parameters

| Niche | Tempo (BPM) | Key Direction | Loop |
|-------|-------------|---------------|------|
| Restaurant | 90-110 | Major, warm | Yes |
| Fashion | 120-140 | Minor/major | Yes |
| Hospitality | 70-90 | Major, airy | Yes |
| Beauty | 80-100 | Major, soft | Yes |
| Events | 128-150 | Minor, heavy bass | Yes |
| Fintech | 100-120 | Neutral, clean | Yes |
| Podcast | 90-110 | Minimal, sharp | Yes |

---

## Prompt Format

```
Create a short loopable brand sound for a [NICHE] campaign.

Mood: [MOOD]
Use case: [3-second tag / 15-second social ad loop / 10-second intro]
Tempo: [BPM]
Style: modern, clean, memorable, minimal, premium
Avoid: vocals, copyrighted melodies, artist imitation, busy drums, long build-ups

The sound should feel like a brand cue people can remember after hearing it once.
```

---

*Internal reference — not for public distribution*
