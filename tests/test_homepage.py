import re
from playwright.sync_api import expect

from pages.login_page import LoginPage


def test_has_title(custom_page):
    custom_page.goto("https://demo.playwright.dev/todomvc/#/")
    # Ensuring title contains substring
    assert "React" in custom_page.title()
    #expect(custom_page).to_have_title(re.compile("React"))

def test_todos_text_box(custom_page):
    custom_page.goto("https://demo.playwright.dev/todomvc/#/")
    custom_page.get_by_placeholder("What needs to be done?").fill("some text")
    custom_page.get_by_placeholder("What needs to be done?").press('Enter')
    #element = custom_page.locator(".filters")
    #assert element.is_visible()
    expect(custom_page.locator(".filters")).to_be_visible()








