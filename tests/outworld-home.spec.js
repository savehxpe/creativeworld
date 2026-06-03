const { test, expect } = require('@playwright/test');

test.describe('Outworld Landing Page — Functional Tests', () => {

  test('1. Homepage loads successfully', async ({ page }) => {
    const response = await page.goto('/');
    expect(response.status()).toBeLessThan(400);
    await expect(page).toHaveTitle(/Outworld Creative/);
  });

  test('2. Hero heading is visible', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('h1')).toBeVisible();
    await expect(page.locator('h1')).toContainText('Outworld Creative');
  });

  test('3. CTA email is visible', async ({ page }) => {
    await page.goto('/');
    const email = page.getByText('team@outworldcreative.com');
    await expect(email.first()).toBeVisible();
  });

  test('4. Logo carousel exists', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByText('Trusted across music, culture and media')).toBeVisible();
  });

  test('5. "What We Do" section exists with 3 cards', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#what-we-do h2')).toBeVisible();
    const cards = page.locator('.capability-card');
    await expect(cards.first()).toBeVisible();
    expect(await cards.count()).toBe(3);
  });

  test('6. Nav logo is visible', async ({ page }) => {
    await page.goto('/');
    await expect(page.locator('#navLogo')).toBeVisible();
  });

  test('7. CTA section exists', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByText('Want sharper ads?')).toBeVisible();
  });

  test('8. Page has no horizontal overflow', async ({ page }) => {
    await page.goto('/');
    const overflow = await page.evaluate(() => ({
      bodyScrollWidth: document.body.scrollWidth,
      windowWidth: window.innerWidth,
    }));
    expect(overflow.bodyScrollWidth).toBeLessThanOrEqual(overflow.windowWidth + 1);
  });

  test('9. Page has no console errors', async ({ page }) => {
    const errors = [];
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    await page.goto('/');
    await page.waitForLoadState('networkidle');
    expect(errors).toHaveLength(0);
  });

});
