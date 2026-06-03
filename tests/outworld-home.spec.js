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

  test('3. HTML contains expected content in source', async ({ page }) => {
    await page.goto('/');
    const html = await page.content();
    expect(html).toContain('Outworld Creative');
    expect(html).toContain('team@outworldcreative.com');
    expect(html).toContain('Want sharper ads?');
    expect(html).toContain('Trusted across music, culture and media');
  });

  test('4. Page has no horizontal overflow', async ({ page }) => {
    await page.goto('/');
    const overflow = await page.evaluate(() => ({
      bodyScrollWidth: document.body.scrollWidth,
      windowWidth: window.innerWidth,
    }));
    expect(overflow.bodyScrollWidth).toBeLessThanOrEqual(overflow.windowWidth + 1);
  });

});
