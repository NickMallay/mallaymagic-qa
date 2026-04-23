from playwright.sync_api import Page
from playwright.sync_api import expect

def test_link_to_about_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="About").click()
    expect(page).to_have_url("https://www.mallaymagic.com/about")


def test_link_to_contact_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="Contact").click()
    expect(page).to_have_url("https://www.mallaymagic.com/contact")

def test_link_to_home_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="Home").click()
    expect(page).to_have_url("https://www.mallaymagic.com")

def test_link_to_birthday_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="Birthday & Family").click()
    expect(page).to_have_url("https://www.mallaymagic.com/birthday")

def test_link_to_lessons_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="Lessons").click()
    expect(page).to_have_url("https://www.mallaymagic.com/lessons")

def test_link_to_free_trick_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="Learn a Free Trick").click()
    expect(page).to_have_url("https://www.mallaymagic.com/free-trick")

def test_link_to_walkaround_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="Walkaround").click()
    expect(page).to_have_url("https://www.mallaymagic.com/walkaround")

def test_link_to_corporate_navigates_successfully(page):
    page.goto("https://www.mallaymagic.com")
    page.get_by_role("navigation").get_by_role("link", name="Corporate Shows").click()
    expect(page).to_have_url("https://www.mallaymagic.com/corporate")


def test_homepage_has_summary(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_test_id("homepage-summary")).to_be_visible()
def test_homepage_cta_visible(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("button", name= "Book a Show")).to_be_visible()
def test_homepage_media(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_test_id("homepage-media")).to_be_visible()