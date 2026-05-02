from playwright.sync_api import Page
from playwright.sync_api import expect

def test_404_has_summary(page):
    page.goto("https://www.mallaymagic.com/404")
    expect(page.get_by_test_id("404-summary")).to_be_visible()