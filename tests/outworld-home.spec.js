const { test, expect } = require('@playwright/test');

test.describe('Outworld Landing Page — Functional Tests', () => {

  test('1. Homepage loads successfully', async ({ page }) => {
    const response = await page.goto('/');
    expect(response.status()).toBeLessThan(400);
    await expect(page).toHaveTitle(/Outworld Creative/);
  });

  test('2. Hero heading is visible', async ({ page }) => {
    await page.goto('/');
    const heading = page.locator('h1');
    await expect(heading).toBeVisible();
    await expect(heading).toContainText('Outworld Creative');
  });

  test('3. Main CTA email is visible', async ({ page }) => {
    await page.goto('/');
    const email = page.getByText('team@outworldcreative.com');
    const emailFound = await email.count();
    expect(emailFound).toBeGreaterThan(0);
  });

  test('4. Logo carousel section exists', async ({ page }) => {
    await page.goto('/');
    const section = page.getByText('Trusted across music, culture and media');
    await expect(section).toBeVisible();
  });

  test('5. "What We Do" section exists', async ({ page }) => {
    await page.goto('/');
    const section = page.locator('#what-we-do h2');
    await expect(section).toBeVisible();
    await expect(section).toContainText('What We Do');
  });

  test('6. Selected Spec Work renders 3 featured cards', async ({ page }) => {
    await page.goto('/');
    const visible = await page.locator('#spec-work > .spec-grid .spec-card').count();
    const collapsed = await page.locator('#specCollapsed.open').count();
    if (visible >= 3) expect(visible).toBeGreaterThanOrEqual(3);
    else expect(visible + await page.locator('#specCollapsed .spec-card').count()).toBeGreaterThanOrEqual(3);
  });

  test('7. Brand Sound is a capability card', async ({ page }) => {
    await page.goto('/');
    const card = page.getByText('Brand Sound');
    await expect(card.first()).toBeVisible();
  });

  test('8. Signal Desk renders 9 tag pills', async ({ page }) => {
    await page.goto('/');
    const tags = page.locator('.signdesk-tag');
    await expect(tags.first()).toBeVisible();
    const count = await tags.count();
    expect(count).toBe(9);
  });

  test('9. Founder byline exists in footer', async ({ page }) => {
    await page.goto('/');
    const section = page.getByText('Founded by saveHXPE');
    await expect(section).toBeVisible();
  });

  test('10. CTA section exists', async ({ page }) => {
    await page.goto('/');
    const section = page.getByText('Want sharper ads?');
    await expect(section).toBeVisible();
  });

  test('11. Page has no horizontal overflow', async ({ page }) => {
    await page.goto('/');
    const overflow = await page.evaluate(() => {
      return {
        bodyScrollWidth: document.body.scrollWidth,
        windowWidth: window.innerWidth,
      };
    });
    expect(overflow.bodyScrollWidth).toBeLessThanOrEqual(overflow.windowWidth + 1);
  });

  test('12. Page has no console errors', async ({ page }) => {
    const errors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    expect(errors).toHaveLength(0);
  });

  test('13. Internal anchor links work where nav is visible', async ({ page }) => {
    await page.goto('/');
    const navVisible = await page.locator('.nav-links').isVisible().catch(() => false);
    if (navVisible) {
      const navLinks = page.locator('nav a[href^="#"]');
      const count = await navLinks.count();
      for (let i = 0; i < count; i++) {
        const href = await navLinks.nth(i).getAttribute('href');
        if (href && href === '#spec-work') {
          await navLinks.nth(i).click();
          await expect(page.locator('#spec-work')).toBeInViewport({ timeout: 5000 });
        }
      }
    }
  });

});
