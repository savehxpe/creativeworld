const { test, expect } = require('@playwright/test');

async function loadAndWait(page, timeout = 15000) {
  await page.goto('/');
  await page.waitForFunction(() => document.querySelector('#root'), { timeout });
}

test.describe('Outworld Landing Page — Visual & Accessibility', () => {

  test.describe('Reduced Motion', () => {
    test.use({
      colorScheme: 'dark',
      reducedMotion: 'reduce',
      viewport: { width: 1440, height: 900 },
    });

    test('Page loads with reduced motion', async ({ page }) => {
      await loadAndWait(page);
      await expect(page.locator('#root')).toBeVisible();
    });

    test('Hero text visible in source', async ({ page }) => {
      await loadAndWait(page);
      const html = await page.content();
      expect(html).toContain('Outworld Creative');
      expect(html).toContain('Video ads and brand sound');
    });

    test('Nav logo img tag exists in source', async ({ page }) => {
      await loadAndWait(page);
      const html = await page.content();
      expect(html).toContain('navLogo');
    });
  });

  test.describe('Screenshots', () => {
    test('Desktop screenshot', async ({ page }) => {
      await loadAndWait(page);
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(3000);
      await expect(page).toHaveScreenshot('desktop-home.png', { fullPage: true, maxDiffPixelRatio: 0.2 });
    });

    test('Mobile screenshot', async ({ page }) => {
      await loadAndWait(page);
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(3000);
      await expect(page).toHaveScreenshot('mobile-home.png', { fullPage: true, maxDiffPixelRatio: 0.2 });
    });

    test('Reduced-motion screenshot', async ({ page }) => {
      await page.emulateMedia({ reducedMotion: 'reduce' });
      await loadAndWait(page);
      await page.waitForLoadState('networkidle');
      await page.waitForTimeout(3000);
      await expect(page).toHaveScreenshot('reduced-motion-home.png', { fullPage: true, maxDiffPixelRatio: 0.2 });
    });
  });

});
