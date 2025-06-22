from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_valid_login(custom_page, user_data):
    custom_page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

    login_page = LoginPage(custom_page)
    login_page.log_into_application(user_data["username"], user_data["password"])

    expect(custom_page.locator("//h2[@class='card-header h5' and text()='My Account']")).to_be_visible()


def test_invalid_login_shows_warning(custom_page):
    custom_page.goto("https://ecommerce-playground.lambdatest.io/index.php?route=account/login")

    login_page = LoginPage(custom_page)
    login_page.log_into_application("wrong@email.com", "wrong-pass")

    warning_text = login_page.get_warning_message()
    expect(custom_page.locator("//div[contains(@class, 'alert-danger')]")).to_be_visible()
    #assert "Warning: No match for E-Mail Address and/or Password." in warning_text
