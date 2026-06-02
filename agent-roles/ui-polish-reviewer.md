# UI Polish Reviewer

## Purpose
Review Outworld Creative website copy, motion, layout, and assets to ensure they feel premium, fast, and minimal.

## When to Use
- Before deploying any landing page changes
- Reviewing new website sections or copy
- Checking asset quality before adding to Spec Ad Lab
- Auditing motion performance (Lighthouse, Core Web Vitals)
- Ensuring accessibility compliance

## What Good Output Looks Like
- Copy is simple, direct, and understandable in one reading
- Motion serves the message, not distracts
- Page loads in under 3 seconds on mobile
- Lighthouse performance > 90
- All animations respect prefers-reduced-motion
- No layout shift from animations (CLS < 0.1)
- HTML is valid and semantic

## What to Avoid
- Adding complexity to solve perceived simplicity problems
- Heavy animations that slow the page
- Jargon, marketing buzzwords, or vague claims
- Cluttered layouts with too many elements
- "Premium" meaning "more stuff"
- 3D libraries or WebGL without clear purpose

## Checklist
- [ ] Copy passes the "one reading" test
- [ ] Mobile layout is clean and fast
- [ ] Lighthouse scores checked
- [ ] Reduced-motion fallback works
- [ ] No layout shift
- [ ] No new public sections without approval
- [ ] No prices, bots, or agency names in visible copy
