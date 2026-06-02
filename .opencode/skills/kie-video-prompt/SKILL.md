# Kie Video Prompt

## Purpose
Turn still-image ad concepts into Seedance 1.5 Pro video prompts. Each prompt describes the 5-second motion that turns a still into a scroll-stopping ad.

## When to Use
- After a Nano Banana 2 still has been generated and selected
- Only for the 3 animated spec ads (#1, #4, #7) initially
- When a still needs to become a video ad for portfolio proof

## Prompt Structure

```
Turn this image into a [duration]-second high-converting social media ad.

[motion description]
Subtle realistic movement: [movement details].
Strong subject focus: [focus description].
First second must feel like a hook: [hook mechanic].
Movement should increase [emotion].
Premium but relatable.
Designed for Instagram Reels, TikTok, Meta Stories, and paid ads.

No random shake.
No warping.
No distorted faces.
No unreadable text.
No unnatural hands.
No fake logos.

Style:
Premium social ad.
Culture-aware.
High-arousal.
Modern African/global creative direction.
Commercial but not corporate.
Sharp, stylish, emotionally clear.
[niche-specific energy].

Duration: [duration] seconds.
Audio: [audio description].
```

## Rules
- Default to `9:16` aspect ratio
- Default to `4` seconds for test, `8` or `12` for final
- Motion must serve the emotion (FOMO = quick, escape = slow)
- First second must create a hook — don't waste it on setup
- Audio direction must be specific, even if `generate_audio` is false
- Never describe impossible motions (no "fly through the plate")

## Quality Check
- [ ] Duration is specified (4, 8, or 12)
- [ ] Motion description is executable (slow push-in, gentle zoom, etc.)
- [ ] First-second hook mechanic is described
- [ ] Emotion is consistent with the still's campaign goal
- [ ] Negative constraints are present
- [ ] Niche-specific energy descriptor is included
