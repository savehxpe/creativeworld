# Seedance 1.5 Pro — Model Reference

Kie.ai Internal Documentation  
Branch: creative-director

---

## Overview

Seedance 1.5 Pro is ByteDance's AI video model, available via Kie.ai API. Supports text-to-video and image-to-video generation with first/last frame control, native audio, and synchronized visuals.

**Use for:** Animating the best spec ad stills into 5-second social ads.

---

## API

### Endpoint
```
POST https://api.kie.ai/api/v1/jobs/createTask
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `model` | string | `bytedance/seedance-1.5-pro` | Model ID |
| `prompt` | string | — | Video generation prompt |
| `image_urls` | array | [] | Up to 2 reference images (input frame) |
| `aspect_ratio` | string | `9:16` | `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `21:9` |
| `duration` | string | `4` | `4`, `8`, `12` seconds |
| `fixed_lens` | boolean | `false` | Lock camera lens |
| `generate_audio` | boolean | `false` | Generate synchronized audio |
| `nsfw_checker` | boolean | `false` | Content safety filter |

---

## Outworld Defaults

```
model: bytedance/seedance-1.5-pro
aspect_ratio: 9:16
duration: "4"
fixed_lens: false
generate_audio: false
nsfw_checker: false
```

---

## Status Polling

```
POST /api/v1/jobs/recordInfo
body: { "taskId": "..." }
```

Typical generation time: 30-120 seconds depending on duration.

---

*Internal reference — not for public distribution*
