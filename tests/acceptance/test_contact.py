from playwright.sync_api import Page
from playwright.sync_api import expect

# Basic page functionality


def test_contact_has_summary(page):
    page.goto("https://www.mallaymagic.com/contact")
    expect(page.get_by_test_id("contact-summary")).to_be_visible()

# Check one of the navbar links, but not all of them, since they are tested in the home page tests
def test_link_to_home_in_navbar(page):
    page.goto("https://www.mallaymagic.com/contact")
    expect(page.get_by_role("navigation").get_by_role("link", name="Home")).to_be_visible()

# Feature specefic tests 
def test_contact_form_visible(page):
    page.goto("https://www.mallaymagic.com/contact")
    expect(page.get_by_role("form", name="Contact Form")).to_be_visible()
def test_booking_form_visible(page):
    page.goto("https://www.mallaymagic.com/contact")
    expect(page.get_by_role("form", name="Booking Form")).to_be_visible()

def test_contact_form_success_confirmation(page):
    page.goto("https://www.mallaymagic.com/contact")
    page.get_by_label("Name").fill("Test User")
    page.get_by_label("Email").fill("email@example.com")
    page.get_by_label("Message").fill("This is a test message.")
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Your message has been submitted.")).to_be_visible()

def test_contact_form_failure_confirmation(page):
    page.get_by_role("button", name="Submit").click()
    expect(page.get_by_text("Please fill out all required fields.")).to_be_visible()

# User Flow informed tests 
