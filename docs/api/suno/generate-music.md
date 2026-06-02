# Generate Music — Model Reference

Suno API Internal Documentation  
Branch: creative-director

---

## Overview

The Generate Music endpoint creates full songs from text prompts. Returns 2 songs per request with stream URLs in ~30-40 seconds and downloadable song URLs in ~2-3 minutes.

**Use for:** Full-length brand anthems, campaign theme songs, creator intros. Not the fastest B2B product for quick brand sounds.

---

## API

### Endpoint
```
POST https://api.sunoapi.org/api/v1/generate/music
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `prompt` | string | — | Text prompt describing the song |
| `model` | string | `V5` | Model version |
| `instrumental` | boolean | `true` | Instrumental only (brand use = instrumental) |
| `make_instrumental` | boolean | `false` | Convert to instrumental |

### Response

```json
{
  "taskId": "...",
  "status": "processing",
  "streams": [],
  "downloads": []
}
```

- Stream URLs: ~30-40 seconds
- Download URLs: ~2-3 minutes
- Output: 2 songs per request

---

## Outworld Defaults

```
model: V5
instrumental: true
make_instrumental: false
```

---

## When to Use

- Brand anthem or theme song (full-length)
- Campaign soundtrack for long-form content
- Creator/podcast intro music
- NOT for quick brand tags or loops (use Generate Sounds endpoint)

---

*Internal reference — not for public distribution*
