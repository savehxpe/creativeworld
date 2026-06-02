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

  test('5. "What We Create" section exists', async ({ page }) => {
    await page.goto('/');
    const section = page.getByText('What We Create').first();
    await expect(section).toBeVisible();
  });

  test('6. Spec Ad Lab renders exactly 9 campaign cards', async ({ page }) => {
    await page.goto('/');
    const cards = page.locator('.spec-card');
    await expect(cards.first()).toBeVisible();
    const count = await cards.count();
    expect(count).toBe(9);
  });

  test('7. Brand Sound section exists', async ({ page }) => {
    await page.goto('/');
    const section = page.getByText('Most brands have visuals');
    await expect(section).toBeVisible();
  });

  test('8. Signal Desk renders exactly 9 pillar cards', async ({ page }) => {
    await page.goto('/');
    const cards = page.locator('.pillar-card');
    await expect(cards.first()).toBeVisible();
    const count = await cards.count();
    expect(count).toBe(9);
  });

  test('9. Founder section exists', async ({ page }) => {
    await page.goto('/');
    const section = page.getByText('Founded by saveHXPE');
    await expect(section).toBeVisible();
  });

  test('10. CTA section exists', async ({ page }) => {
    await page.goto('/');
    const section = page.getByText('For Brand Work');
    await expect(section).toBeVisible();
  });

  test('11. Page has no horizontal overflow', async ({ page }) => {
    await page.goto('/');
    const overflow = await page.evaluate(() => {
      return {
        bodyScrollWidth: document.body.scrollWidth,
        windowWidth: window.innerWidth,
        htmlScrollWidth: document.documentElement.scrollWidth,
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
    
    // Check if nav links are visible (they hide at 768px breakpoint)
    const navVisible = await page.locator('.nav-links').isVisible().catch(() => false);
    
    if (navVisible) {
      const navLinks = page.locator('nav a[href^="#"]');
      const count = await navLinks.count();
      for (let i = 0; i < count; i++) {
        const href = await navLinks.nth(i).getAttribute('href');
        await navLinks.nth(i).click();
        if (href && href !== '#') {
          await expect(page.locator(href)).toBeInViewport({ timeout: 5000 });
        }
      }
    }
    // Mobile/tablet: nav hidden is expected behavior at < 768px
  });

});
