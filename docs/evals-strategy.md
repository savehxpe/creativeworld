# Evals Strategy

Outworld Creative — Internal Quality System  
Branch: creative-director

---

## Purpose

Use PromptFoo-style evals to test whether Outworld outputs are clear, premium, useful, direct, and not generic — before they reach a client.

---

## How It Works

Each eval file defines prompts and rubrics. A grading model scores each output against each rubric item. Failed items block the output from being used with clients.

---

## Hard Fails (Score = 0 — Output is Rejected)

- **no-fake-claims:** Contains false statistics, made-up case studies, or unverifiable results
- **no-conspiracy:** Contains secret control, occult, or unnamed-power-group language
- **no-prices:** Contains pricing information in public-facing output
- **no-bot-automation-language:** Contains "AI bot," "automation," or "we use AI to do everything" language

## Soft Fails (Score < expected — Output Needs Revision)

- **clarity:** Can a brand owner understand this in one reading?
- **usefulness:** Does this actually help the brand, or is it just interesting?
- **specificity:** Is this tailored to the niche and market?
- **no-generic-claims:** Avoids vague claims like "make you look premium"

---

## Eval Files

| File | Tests |
|------|-------|
| `evals/promptfoo/spec-ad-lab.yaml` | Spec ad concepts |
| `evals/promptfoo/outreach.yaml` | Outreach messages |
| `evals/promptfoo/brand-sound.yaml` | Brand sound concepts |
| `evals/promptfoo/signal-desk.yaml` | Signal Desk content |

---

## When to Run Evals

- Before sending any client-facing creative output
- Before publishing Signal Desk content
- During creative director workflow: generate → evaluate → revise → evaluate → deliver
- Weekly: re-evaluate a random sample of outputs to catch quality drift

---

*Internal document — not for public distribution*
