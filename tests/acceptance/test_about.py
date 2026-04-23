from playwright.sync_api import Page
from playwright.sync_api import expect

# Basic page functionality

def test_about_has_summary(page):
    page.goto("https://www.mallaymagic.com/about")
    expect(page.get_by_test_id("about-summary")).to_be_visible()
def test_about_has_FAQ(page):
    page.goto("https://www.mallaymagic.com/about")
    expect(page.get_by_test_id("about-faq")).to_be_visible()
# Feature specefic tests 
# User Flow informed tests 