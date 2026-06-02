# Playwright Testing

Outworld Creative — Test Suite  
Branch: creative-director

---

## Overview

End-to-end test suite for the Outworld Creative landing page using Playwright. Covers functional, responsive, accessibility, and visual testing.

---

## Setup

```bash
npm i -D @playwright/test
npx playwright install chromium
```

---

## Test Structure

| File | Purpose |
|------|---------|
| `playwright.config.js` | Global config — 3 viewports (desktop/tablet/mobile), local static server on port 3000 |
| `tests/outworld-home.spec.js` | 13 functional tests + responsive validation |
| `tests/outworld-visual.spec.js` | Reduced-motion accessibility + screenshot baselines |

---

## Run Commands

```bash
# Run all tests
npm run test:e2e

# Run in headed mode (see browser)
npm run test:e2e:headed

# View HTML report
npm run test:e2e:report

# Run specific test file
npx playwright test tests/outworld-home.spec.js
```

---

## Viewports Tested

| Name | Resolution |
|------|-----------|
| Desktop | 1440 × 900 |
| Tablet | 768 × 1024 |
| Mobile | 390 × 844 |

---

## Functional Tests (13)

1. Homepage loads successfully (status < 400)
2. Hero heading "Outworld Creative" visible
3. CTA email `team@outworldcreative.com` visible
4. Logo carousel section exists
5. "What We Create" section exists
6. Spec Ad Lab renders exactly 9 campaign cards
7. Brand Sound section exists
8. Signal Desk renders exactly 9 pillar cards
9. Founder section exists
10. CTA section "For Brand Work" exists
11. No horizontal overflow on mobile
12. No console errors
13. Internal anchor links navigate correctly

---

## Visual & Accessibility Tests

- Reduced-motion: page loads successfully
- Reduced-motion: hero text visible without animation
- Reduced-motion: loader hidden after load
- Desktop screenshot baseline
- Mobile screenshot baseline
- Reduced-motion screenshot baseline

---

## Screenshot Baselines

First run creates baselines at `tests/outworld-visual.spec.js-snapshots/`. Subsequent runs compare against baselines. To update baselines after intentional changes:

```bash
npx playwright test --update-snapshots
```

---

*Internal document — not for public distribution*
