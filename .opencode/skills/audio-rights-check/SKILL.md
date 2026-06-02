# Audio Rights Check

## Purpose
Check whether generated audio is safe to sell based on account tier, generation date, model, and usage notes. This is a mandatory gate — no audio asset leaves Outworld without passing this check.

## When to Use
- Before delivering any Suno-generated sound to a client
- Before including any generated audio in a portfolio (commercial vs. non-commercial use)
- When building Brand Sound Packs for paid clients
- Periodically, to audit existing sound library

## The 5 Gates

### Gate 1: Account Eligibility
- Was the sound generated under a commercial-use eligible Suno account? (Pro or Premier)
- Was the account in Pro/Premier status at the time of generation?
- **Free-tier songs are for non-commercial use only.** Subscribing later does NOT grant retroactive rights.

### Gate 2: Generation Records
- Is the prompt text recorded?
- Is the generation date recorded?
- Is the model version recorded?
- Is the task ID recorded?

### Gate 3: Content Safety
- No artist names in the prompt
- No imitation of existing jingles or brand sounds
- No copied melodies or recognizable samples
- Output is original enough to not trigger infringement

### Gate 4: Client Delivery
- Client receives a usage license (not "ownership")
- License terms are clear (territory, duration, media)
- Producer has edited/finished the output before delivery
- Finished product contains meaningful human authorship

### Gate 5: Legal Disclaimers
- Not promising copyright registration
- Not calling output "exclusive" unless license allows AND file is customized
- Not claiming "royalty-free" unless all rights are controlled
- No recognizable samples without clearance

## Pass/Fail
- **ALL must pass.** Any failure = sound NOT cleared for commercial delivery.
- Failed sounds: internal reference or portfolio proof (non-commercial) only.
- Re-generate with a commercial-eligible account if needed.

## Record Template
```
# Audio Rights Record
Sound Name: [name]
Task ID: [id]
Generated: [date]
Account Tier: [Pro/Premier]
Model: [V5]
Prompt: [prompt text]
Checklist: all passed
Delivery Status: Approved
```
