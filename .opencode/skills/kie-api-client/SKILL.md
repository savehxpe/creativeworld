# Kie API Client

## Purpose
Call the Kie API safely using the API key from `.env`, create tasks, poll task status, and save output URLs. Never expose the key.

## When to Use
- Generating spec ad stills with Nano Banana 2
- Animating stills with Seedance 1.5 Pro
- Motion-controlled video with Kling 3.0 (future)
- Checking task status during generation
- Any Kie API interaction in Outworld Creative workflows

## API Reference

### Environment Variable
- `KIE_AI_API` — API key loaded from `.env` via `dotenv`

### Endpoint
- `POST https://api.kie.ai/api/v1/jobs/createTask` — Create generation task
- `POST https://api.kie.ai/api/v1/jobs/recordInfo` — Get task details/status

### Functions

#### `createNanoBananaTask(input)`
Generates still images.
- `input.prompt` — Text prompt
- `input.aspect_ratio` — Default `4:5`
- `input.resolution` — Default `1K` (options: `1K`, `2K`, `4K`)
- `input.output_format` — Default `jpg` (options: `png`, `jpg`)

#### `createSeedanceTask(input)`
Generates video from text or image.
- `input.prompt` — Text prompt
- `input.image_urls` — Optional array of reference image URLs (up to 2)
- `input.aspect_ratio` — Default `9:16`
- `input.duration` — Default `4` (options: `4`, `8`, `12`)
- `input.generate_audio` — Default `false`

#### `createKlingMotionTask(input)`
Motion-controlled video (requires image + video).
- `input.image_urls` — Required: reference images
- `input.video_urls` — Required: motion video
- `input.mode` — Default `720p`

#### `getTaskDetails(taskId)`
Poll task status and get output URLs.

## Safety Rules
- Never log or print `process.env.KIE_AI_API`
- Never commit `.env` to git
- Rotate the key if ever exposed in logs or commits
- Use the Node.js client at `lib/kie/client.js` — not raw API calls

## Quality Check
- [ ] API key is loaded from environment only
- [ ] No key appears in console output
- [ ] Task IDs are logged for status tracking
- [ ] Error messages don't leak auth headers
- [ ] `.env` is in `.gitignore`
