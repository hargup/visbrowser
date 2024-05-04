import time
import pytesseract
from PIL import Image
from playwright.sync_api import Page, expect, sync_playwright
from visbrowser import click, hover, wait_for_text
import re

def test_wait_for_text(page: Page):
    page.goto("https://example.com")
    assert wait_for_text(page, "Example", timeout=5)
    assert not wait_for_text(page, "Nonexistent", timeout=2)

def test_click(page: Page):
    page.goto("https://example.com")
    click(page, "More information")
    expect(page).to_have_url(re.compile(r"https://example\.com/info/.*"))

def test_hover(page: Page):
    page.goto("https://example.com")
    hover(page, "Menu")
    expect(page.locator(".submenu")).to_be_visible()

# Run tests
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    test_wait_for_text(page)
    test_click(page)
    test_hover(page)
    browser.close()