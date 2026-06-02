# Nano Banana 2 — Model Reference

Kie.ai Internal Documentation  
Branch: creative-director

---

## Overview

Nano Banana 2 is Google's Gemini Flash image model, available via Kie.ai API. Best for fast, affordable still-image generation with good text rendering, character consistency, and scalable workflows.

**Use for:** Spec ad stills, campaign visuals, mock ad frames.

---

## API

### Endpoint
```
POST https://api.kie.ai/api/v1/jobs/createTask
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | `nano-banana-2` | Model ID |
| `prompt` | string | — | Text prompt for image generation |
| `aspect_ratio` | string | `4:5` | `4:5`, `9:16`, `1:1`, `16:9` |
| `resolution` | string | `1K` | `1K`, `2K`, `4K` |
| `output_format` | string | `jpg` | `png` or `jpg` |
| `image_urls` | array | [] | Up to 14 reference images for editing/iteration |

### Pricing
- 1K: $0.04/image
- 2K: $0.06/image
- 4K: $0.09/image

---

## Outworld Defaults

```
model: nano-banana-2
aspect_ratio: 4:5
resolution: 1K
output_format: jpg
```

---

## Status Polling

```
POST /api/v1/jobs/recordInfo
body: { "taskId": "..." }
```

Typical generation time: 5-30 seconds.

---

*Internal reference — not for public distribution*
