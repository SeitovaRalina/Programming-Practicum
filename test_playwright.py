import re
from playwright.sync_api import Page, expect

def test_homepage_has_Playwright(page: Page):
    # connect to the target page
    page.goto("https://playwright.dev/")

    # expect the page title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))