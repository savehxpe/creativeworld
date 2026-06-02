# Kling 3.0 Motion Control — Model Reference

Kie.ai Internal Documentation  
Branch: creative-director

---

## Overview

Kling 3.0 Motion Control enables controlled video generation using a reference image and a motion video. The model transfers motion from the video onto the subject in the image.

**Use for:** Advanced motion control when Seedance results need more precise movement. Requires existing motion video reference.

**Do not start with Kling.** It requires both an image URL and a motion video URL. Use Nano Banana 2 for stills and Seedance 1.5 Pro for animation first.

---

## API

### Endpoint
```
POST https://api.kie.ai/api/v1/jobs/createTask
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | `kling-3.0/motion-control` | Model ID |
| `image_urls` | array | — | Reference image URLs (required) |
| `video_urls` | array | — | Motion video URLs (required) |
| `mode` | string | `720p` | Resolution mode |
| `character_orientation` | string | `video` | Character orientation source |
| `background_source` | string | `input_video` | Background source |

### File Size Limits
- Images: under 10MB
- Videos: under 100MB

---

## Outworld Defaults

```
model: kling-3.0/motion-control
mode: 720p
character_orientation: video
background_source: input_video
```

---

## When to Use

- After Nano Banana 2 stills look right
- After Seedance 1.5 Pro animation looks close but needs precision
- When you have a specific motion reference video
- For controlled camera movements that Seedance can't achieve

---

*Internal reference — not for public distribution*
