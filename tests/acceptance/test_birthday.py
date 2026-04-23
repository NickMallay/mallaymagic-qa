from playwright.sync_api import Page
from playwright.sync_api import expect

# Basic page functionality
# Check one of the navbar links, but not all of them, since they are tested in the home page tests
def test_link_to_home_in_navbar(page):
    page.goto("https://www.mallaymagic.com/birthday")
    expect(page.get_by_role("navigation").get_by_role("link", name="Home")).to_be_visible()
def test_birthday_has_summary(page):
    page.goto("https://www.mallaymagic.com/birthday")
    expect(page.get_by_test_id("birthday-summary")).to_be_visible()
def test_birthday_has_CTA(page):
    page.goto("https://www.mallaymagic.com/birthday")
    expect(page.get_by_test_id("birthday-cta")).to_be_visible()
# Feature specefic tests 
# User Flow informed tests 