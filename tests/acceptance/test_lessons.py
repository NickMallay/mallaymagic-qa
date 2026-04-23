from playwright.sync_api import Page
from playwright.sync_api import expect

# Basic page functionality

def test_lessons_has_summary(page):
    page.goto("https://www.mallaymagic.com/lessons")
    expect(page.get_by_test_id("lessons-summary")).to_be_visible()
def test_lessons_has_CTA(page):
    page.goto("https://www.mallaymagic.com/lessons")
    expect(page.get_by_test_id("lessons-cta")).to_be_visible()
# Feature specefic tests 
# User Flow informed tests 