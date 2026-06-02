# Security Reviewer

## Purpose
Audit the Outworld Creative repository for security risks: exposed keys, committed secrets, `.env` hygiene, API key safety, and git history leaks.

## When to Use
- Before any commit that touches configuration or API code
- After adding or rotating API keys
- Periodically (weekly) to check for accidental secret exposure
- Before pushing to a public remote
- When adding new environment variables

## What Good Output Looks Like
- `.env` is in `.gitignore` and not tracked by git
- No API keys, tokens, or secrets in committed files
- Git history has been audited for previously exposed keys
- All exposed keys have been rotated
- New environment variables are documented but values are never committed
- Client code reads from `process.env` — never hardcoded

## What to Avoid
- Printing, logging, or echoing API keys to terminal
- Committing `.env` or any config file with actual secrets
- Hardcoding API keys in source files
- Copying `.env` values into chat messages
- Using the same key after it's been exposed in git history

## Checklist
- [ ] `.gitignore` includes `.env`, `node_modules/`
- [ ] `git status` shows `.env` as untracked or absent
- [ ] No API keys visible in `git log -p`
- [ ] Client code uses `process.env.VAR_NAME`
- [ ] Exposed keys have been rotated at source
- [ ] No secrets printed to terminal output
