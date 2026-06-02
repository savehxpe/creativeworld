# Deployment Checklist

Outworld Creative — Public Landing Page  
Branch: creative-director

---

## 1. Push to GitHub

```bash
cd /Users/tshepomotolo/ole/outworld

# Add remote (if not already configured)
git remote add origin https://github.com/savehxpe/creativeworld.git

# Push the creative-director branch
git push -u origin creative-director
```

---

## 2. Import on Vercel

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click "Import" → select the `creativeworld` repo
3. Configure:

| Setting | Value |
|---------|-------|
| Framework Preset | **Other** |
| Root Directory | `./` |
| Install Command | `npm install` |
| Build Command | `npm run build` |
| Output Directory | `dist` |
| Environment Variables | None needed |

4. Click "Deploy"

---

## 3. Connect Custom Domain

1. Vercel Dashboard → Project → Settings → Domains
2. Add: `outworldcreative.com`
3. Follow Vercel's DNS instructions to add a CNAME record in Namecheap
4. Wait for SSL certificate auto-provisioning (~1-2 minutes)

---

## 4. Verify Internal Files Are NOT Publicly Served

After deployment, visit the following URLs. All should return 404 or not be accessible:

```
https://your-project.vercel.app/docs/
https://your-project.vercel.app/skills/
https://your-project.vercel.app/memory/
https://your-project.vercel.app/scripts/
https://your-project.vercel.app/lib/
https://your-project.vercel.app/.env
```

The `build` script copies only `landing_page/` into `dist/`. No internal files are exposed.

---

## 5. Live Deployment Verification

- [ ] Landing page loads at Vercel URL
- [ ] Hero section visible with logo + waveform
- [ ] Logo carousel scrolls smoothly
- [ ] "What We Create" cards present (18 cards)
- [ ] Spec Ad Lab shows 9 campaign cards
- [ ] Brand Sound section visible with sound-wave animation
- [ ] Signal Desk shows 9 pillar cards
- [ ] Founder section present
- [ ] CTA "Want sharper ads?" + email link works
- [ ] Logo renders white on dark background
- [ ] Mobile layout is clean (test on phone)
- [ ] No horizontal overflow
- [ ] Console has no errors

---

*Internal document — not for public distribution*
