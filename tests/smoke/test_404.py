from playwright.sync_api import Page
from playwright.sync_api import expect

def test_404(page):
    response = page.goto("https://www.mallaymagic.com/this-is-not-real")
    assert response.status == 404

