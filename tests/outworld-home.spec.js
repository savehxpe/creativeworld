const { test, expect } = require('@playwright/test');

test.describe('Outworld Landing Page — Functional Tests', () => {

  test('1. Homepage loads successfully', async ({ page }) => {
    const response = await page.goto('/');
    expect(response.status()).toBeLessThan(400);
    await expect(page).toHaveTitle(/Outworld Creative/);
  });

  test('2. HTML has expected React mount point', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#root')).toBeVisible();
  });

  test('3. Page contains expected visible text', async ({ page }) => {
    await page.goto('/');
    await page.waitForTimeout(2000);
    await expect(page.locator('.hero-headline')).toContainText('Outworld Creative');
    await expect(page.locator('.hero-email')).toContainText('team@outworldcreative.com');
    await expect(page.locator('#final-cta')).toContainText('Ideas that');
    await expect(page.locator('#final-cta')).toContainText('stick');
    await expect(page.locator('.hero-cta')).toContainText('Request a Creative Diagnosis');
  });

  test('4. Page has no horizontal overflow', async ({ page }) => {
    await page.goto('/');
    const overflow = await page.evaluate(() => ({
      bodyScrollWidth: document.body.scrollWidth,
      windowWidth: window.innerWidth,
    }));
    expect(overflow.bodyScrollWidth).toBeLessThanOrEqual(overflow.windowWidth + 1);
  });

  test('5. Hero video exists and has correct attributes', async ({ page }) => {
    await page.goto('/');
    const video = page.locator('#heroVideo');
    await expect(video).toBeAttached();
    const html = await page.content();
    expect(html).toContain('muted');
    expect(html).toContain('playsinline');
    const poster = await video.getAttribute('poster');
    expect(poster).toContain('outworld-scroll-hero-poster.jpg');
    const controls = await video.getAttribute('controls');
    expect(controls).toBeNull();
  });

  test('6. Progress line exists', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#heroProgressLine')).toBeAttached();
  });

  test('7. Hero content is visible and not overlapped by nav', async ({ page }) => {
    await page.goto('/');
    await page.waitForTimeout(2000); // let animations settle
    const headline = page.locator('.hero-headline');
    await expect(headline).toBeVisible();
    const box = await headline.boundingBox();
    expect(box.y).toBeGreaterThan(80); // should be below nav
  });

  test('8. CTA email is visible', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('span.hero-email a[href="mailto:team@outworldcreative.com"]')).toBeVisible();
  });

  test('9. No console errors on load', async ({ page }) => {
    const errors = [];
    page.on('pageerror', err => errors.push(err.message));
    await page.goto('/');
    await page.waitForTimeout(3000);
    expect(errors).toHaveLength(0);
  });

  test('10. Reduced motion shows static poster and disables scrub', async ({ page }) => {
    await page.emulateMedia({ reducedMotion: 'reduce' });
    await page.goto('/');
    await page.waitForTimeout(1000);
    const video = page.locator('#heroVideo');
    await expect(video).toBeAttached();
    const progressLine = page.locator('#heroProgressLine');
    const display = await progressLine.evaluate(el => window.getComputedStyle(el).display);
    expect(display).toBe('none');
  });

});
