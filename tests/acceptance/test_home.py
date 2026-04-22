from playwright.sync_api import Page
from playwright.sync_api import expect

def test_link_to_about_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="About + FAQ")).to_be_visible()
def test_link_to_contact_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="Contact")).to_be_visible()
def test_link_to_home_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="Home")).to_be_visible()
def test_link_to_birthday_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="Birthday & Family")).to_be_visible()
def test_link_to_lessons_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="Lessons")).to_be_visible()
def test_link_to_freebee_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="Learn a Trick Now")).to_be_visible()
def test_link_to_walkaround_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="Walkaround")).to_be_visible()
def test_link_to_corporate_in_navbar(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("navigation").get_by_role("link", name="Corporate Shows")).to_be_visible()
def test_homepage_has_summary(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_test_id("homepage-summary")).to_be_visible()
def test_homepage_cta_visible(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_role("button", name= "Book a Show")).to_be_visible()
def test_homepage_media(page):
    page.goto("https://www.mallaymagic.com")
    expect(page.get_by_test_id("homepage-media")).to_be_visible()