"""
Accessibility Tree Playground for browser-use

- Launches a browser and navigates to a target URL (default: amazon.com)
- Extracts the aria snapshot using Playwright
- Prints the snapshot
- Easy to modify for your own experiments

Run with: python browser_use/dom/tests/test_accessibility_playground.py
"""

import asyncio

from browser_use.browser.types import async_playwright

# Change this to any site you want to test


async def get_ax_tree(TARGET_URL):
	async with async_playwright() as p:
		browser = await p.chromium.launch(headless=True)
		page = await browser.new_page()
		print(f'Navigating to {TARGET_URL}')
		await page.goto(TARGET_URL, wait_until='domcontentloaded')

		ax_snapshot = await page.aria_snapshot()
		print(ax_snapshot)
		print(f'length of aria snapshot: {len(ax_snapshot)}')

		await browser.close()


if __name__ == '__main__':
	TARGET_URL = [
		# 'https://amazon.com/',
		# 'https://www.google.com/',
		# 'https://www.facebook.com/',
		# 'https://platform.openai.com/tokenizer',
		'https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox',
	]
	for url in TARGET_URL:
		asyncio.run(get_ax_tree(url))
