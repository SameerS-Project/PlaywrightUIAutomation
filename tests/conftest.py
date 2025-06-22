import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def custom_page():
    #   Browser instance for testing
    print("\nLaunching browser and opening page...")
    with sync_playwright() as playwright:
        browser = playwright.firefox.launch(headless=True)
        page = browser.new_page()
        yield page
        browser.close()

@pytest.fixture(scope="function")
def user_data():
    print("\nSetting up user data..")
    data = {"username": "postrona93@gmail.com", "password": "123@Best"}
    yield data
    print("Tearing down user data...")