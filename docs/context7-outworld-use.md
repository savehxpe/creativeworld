# Context7 CLI — Outworld Creative Use

Internal document — not for public distribution

---

## Purpose

Context7 fetches current library documentation before implementation. At Outworld, we use it to ensure every frontend and deployment change is based on real, up-to-date docs — not guesswork.

---

## When to Use Context7

**Before implementing any change involving these libraries:**

| Library | Use in Outworld |
|---------|----------------|
| Tailwind CSS | Landing page styling (CDN) |
| React 18 | UMD-based SPA in index.html |
| Framer Motion | BlurText animation, future motion |
| GSAP | Future scroll animations (not yet used) |
| Playwright | E2E testing |
| Vercel | Deployment config |

---

## Rules

- Before using any library API, fetch docs first.
- Do not guess animation APIs.
- Do not guess Playwright syntax.
- Do not guess Vercel config.
- Do not add libraries without checking docs.

---

## Preferred Docs Workflow

```
1. Context7 docs first
2. Implement small change
3. Run build
4. Run Playwright
5. Commit only after tests pass
```

---

## Installed As

- Skill name: `context7-cli`
- Path: `.agents/skills/context7-cli/`
- Invoked via: `$context7-cli` or loaded by the agent

---

## Quick Reference

```bash
# Fetch Tailwind docs
context7 tailwind

# Fetch React docs
context7 react

# Fetch Playwright docs
context7 playwright

# Fetch Vercel docs
context7 vercel
```

---

*Internal document — not for public distribution*
