from playwright.sync_api import Page
from playwright.sync_api import expect

def test_corporate_page_title(page):
    page.goto("https://www.mallaymagic.com/corporate")
    expect(page).to_have_title("Mallay Magic")