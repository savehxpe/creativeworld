const { test, expect } = require('@playwright/test');

test.describe('Outworld Landing Page — Visual & Accessibility', () => {

  test.describe('Reduced Motion', () => {
    test.use({
      colorScheme: 'dark',
      reducedMotion: 'reduce',
      viewport: { width: 1440, height: 900 },
    });

    test('Page loads with reduced motion', async ({ page }) => {
      await page.goto('/');
      await expect(page.locator('h1')).toBeVisible();
    });

    test('Hero text visible without relying on animation', async ({ page }) => {
      await page.goto('/');
      await page.waitForTimeout(1000);
      await expect(page.locator('h1')).toBeVisible();
      await expect(page.getByText('Video ads and brand sound for brands')).toBeVisible();
    });

    test('Nav logo visible with reduced motion', async ({ page }) => {
      await page.goto('/');
      await page.waitForLoadState('networkidle');
      await expect(page.locator('#navLogo')).toBeVisible();
    });
  });

  test.describe('Screenshots', () => {
    test('Desktop screenshot', async ({ page }) => {
      await page.goto('/');
      await page.waitForLoadState('networkidle');
      await expect(page).toHaveScreenshot('desktop-home.png', { fullPage: true, maxDiffPixelRatio: 0.2 });
    });

    test('Mobile screenshot', async ({ page }) => {
      await page.goto('/');
      await page.waitForLoadState('networkidle');
      await expect(page).toHaveScreenshot('mobile-home.png', { fullPage: true, maxDiffPixelRatio: 0.2 });
    });

    test('Reduced-motion screenshot', async ({ page }) => {
      await page.emulateMedia({ reducedMotion: 'reduce' });
      await page.goto('/');
      await page.waitForLoadState('networkidle');
      await expect(page).toHaveScreenshot('reduced-motion-home.png', { fullPage: true, maxDiffPixelRatio: 0.2 });
    });
  });

});
