from playwright.sync_api import Page
from playwright.sync_api import expect

# Basic page functionality

def test_free_trick_has_summary(page):
    page.goto("https://www.mallaymagic.com/free-trick")
    expect(page.get_by_test_id("free-trick-summary")).to_be_visible()
def test_free_trick_has_CTA(page):
    page.goto("https://www.mallaymagic.com/free-trick")
    expect(page.get_by_test_id("free-trick-cta")).to_be_visible()
# Feature specefic tests

def test_email_success_confirmation(page):
    page.goto("https://www.mallaymagic.com/free-trick")
    page.get_by_label("Email").fill("email@example.com")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_test_id("email-gate")).to_be_hidden()
    expect(page.get_by_test_id("free-trick-content")).to_be_visible()
def test_free_trick_hidden_until_email_submitted(page):
    page.goto("https://www.mallaymagic.com/free-trick")
    expect(page.get_by_test_id("free-trick-content")).to_be_hidden()
    expect(page.get_by_test_id("email-gate")).to_be_visible()
def test_email_failure_confirmation(page):
    page.goto("https://www.mallaymagic.com/free-trick")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Please enter a valid email address.")).to_be_visible()
# User Flow informed tests 